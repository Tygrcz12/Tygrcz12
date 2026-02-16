#!/usr/bin/env python3
"""
YouTube Video/Audio Downloader
A command-line tool to download videos from YouTube in MP3 or MP4 format.
"""

import os
import sys

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp is not installed.")
    print("Please install it using: pip install yt-dlp")
    sys.exit(1)


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner():
    """Print the application banner."""
    print("=" * 60)
    print("           YouTube Video/Audio Downloader")
    print("=" * 60)
    print()


def get_url():
    """Get YouTube URL from user."""
    while True:
        url = input("Enter YouTube URL (or 'q' to quit): ").strip()
        if url.lower() == 'q':
            return None
        if url:
            return url
        print("Error: URL cannot be empty. Please try again.\n")


def get_format():
    """Get desired format from user."""
    print("\nSelect download format:")
    print("1. MP3 (Audio only)")
    print("2. MP4 (Video)")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        if choice == '1':
            return 'mp3', None
        elif choice == '2':
            quality = get_video_quality()
            return 'mp4', quality
        else:
            print("Error: Invalid choice. Please enter 1 or 2.")


def get_video_quality():
    """Get desired video quality from user."""
    print("\nSelect video quality:")
    print("1. Best available (highest quality)")
    print("2. 1080p (Full HD)")
    print("3. 720p (HD)")
    print("4. 480p (SD)")
    print("5. 360p (Low)")
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == '1':
            return 'best'
        elif choice == '2':
            return '1080'
        elif choice == '3':
            return '720'
        elif choice == '4':
            return '480'
        elif choice == '5':
            return '360'
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 5.")


def download_video(url, format_type, quality=None):
    """
    Download video from YouTube.
    
    Args:
        url: YouTube video URL
        format_type: 'mp3' or 'mp4'
        quality: Video quality ('best', '1080', '720', '480', '360') for MP4
    """
    try:
        # Create downloads folder if it doesn't exist
        download_path = os.path.join(os.getcwd(), 'downloads')
        os.makedirs(download_path, exist_ok=True)
        
        print(f"\nDownloading as {format_type.upper()}...")
        if format_type == 'mp4' and quality:
            quality_text = 'Best available' if quality == 'best' else f'{quality}p'
            print(f"Quality: {quality_text}")
        print("Please wait...\n")
        
        if format_type == 'mp3':
            # Download as audio (MP3)
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                'quiet': False,
                'no_warnings': False,
            }
        else:
            # Download as video (MP4) with specified quality
            if quality == 'best':
                # Download best quality available
                format_string = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            else:
                # Download specific resolution, fallback to best if not available
                format_string = (
                    f'bestvideo[height<={quality}][ext=mp4]+bestaudio[ext=m4a]/'
                    f'best[height<={quality}][ext=mp4]/'
                    'bestvideo[ext=mp4]+bestaudio[ext=m4a]/'
                    'best[ext=mp4]/best'
                )
            
            ydl_opts = {
                'format': format_string,
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                'quiet': False,
                'no_warnings': False,
            }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Unknown')
            print(f"\n✓ Successfully downloaded: {title}")
            print(f"✓ Saved to: {download_path}\n")
            
        return True
        
    except yt_dlp.utils.DownloadError as e:
        print(f"\n✗ Download error: {e}")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return False


def main():
    """Main application loop."""
    clear_screen()
    print_banner()
    
    print("Note: This tool downloads videos to a 'downloads' folder")
    print("      in the current directory.\n")
    print("Note: MP3 conversion requires FFmpeg to be installed.")
    print("      If you don't have FFmpeg, videos will be downloaded")
    print("      in their original audio format.\n")
    
    while True:
        # Get URL from user
        url = get_url()
        if url is None:
            print("\nThank you for using YouTube Downloader!")
            break
        
        # Get format and quality from user
        format_type, quality = get_format()
        
        # Download the video
        success = download_video(url, format_type, quality)
        
        # Ask if user wants to download another video
        print()
        another = input("Download another video? (y/n): ").strip().lower()
        if another != 'y':
            print("\nThank you for using YouTube Downloader!")
            break
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDownload interrupted by user.")
        sys.exit(0)
