#!/usr/bin/env python3
"""
YouTube Video/Audio Downloader
A command-line tool to download videos from YouTube in MP3 or MP4 format.
"""

import os
import sys
import shutil

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp is not installed.")
    print("Please install it using: pip install yt-dlp")
    sys.exit(1)


def check_ffmpeg():
    """Check if FFmpeg is installed."""
    return shutil.which('ffmpeg') is not None


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
        # Check if FFmpeg is available
        has_ffmpeg = check_ffmpeg()
        
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
            if not has_ffmpeg:
                print("⚠ Warning: FFmpeg not found. Downloading audio in original format instead of MP3.")
                print("   Install FFmpeg to enable MP3 conversion.\n")
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                    'quiet': False,
                    'no_warnings': False,
                }
            else:
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
            if not has_ffmpeg:
                # Without FFmpeg, we can't merge video+audio, so download pre-merged formats only
                print("⚠ Warning: FFmpeg not found. Downloading single-file format (may not be highest quality).")
                print("   Install FFmpeg to enable high-quality downloads with separate video/audio merging.\n")
                
                if quality == 'best':
                    format_string = 'best[ext=mp4]/best'
                else:
                    format_string = f'best[height<={quality}][ext=mp4]/best[height<={quality}]/best[ext=mp4]/best'
            else:
                # With FFmpeg, we can merge video+audio for better quality
                if quality == 'best':
                    format_string = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
                else:
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
    
    # Check FFmpeg availability
    has_ffmpeg = check_ffmpeg()
    
    print("Note: This tool downloads videos to a 'downloads' folder")
    print("      in the current directory.\n")
    
    if has_ffmpeg:
        print("✓ FFmpeg detected: Full functionality available")
        print("  - MP3 conversion enabled")
        print("  - High-quality video downloads with audio merging enabled\n")
    else:
        print("⚠ FFmpeg not detected: Limited functionality")
        print("  - MP3 conversion disabled (audio will download in original format)")
        print("  - High-quality downloads disabled (single-file formats only)")
        print("  - To enable full features, install FFmpeg:")
        print("    • Windows: Download from ffmpeg.org and add to PATH")
        print("    • Linux: sudo apt-get install ffmpeg")
        print("    • macOS: brew install ffmpeg\n")
    
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
