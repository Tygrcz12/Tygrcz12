# YouTube Video/Audio Downloader

A simple command-line tool to download videos from YouTube in MP3 (audio) or MP4 (video) format.

## Features

- Download YouTube videos in MP4 format
- Extract audio and save as MP3 format
- User-friendly command-line interface
- Downloads saved to a dedicated 'downloads' folder
- Simple URL input and format selection

## Requirements

- Python 3.6 or higher
- yt-dlp library
- FFmpeg (optional, required for MP3 conversion)

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. (Optional) Install FFmpeg for MP3 conversion:
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - **Linux**: `sudo apt-get install ffmpeg`
   - **macOS**: `brew install ffmpeg`

## Usage

1. Run the downloader:
```bash
python youtube_downloader.py
```

2. Follow the prompts:
   - Enter the YouTube video URL
   - Select the format:
     - `1` for MP3 (audio only)
     - `2` for MP4 (video)
   - Wait for the download to complete

3. Find your downloaded files in the `downloads` folder

## Example

```
==============================================================
           YouTube Video/Audio Downloader
==============================================================

Note: This tool downloads videos to a 'downloads' folder
      in the current directory.

Note: MP3 conversion requires FFmpeg to be installed.
      If you don't have FFmpeg, videos will be downloaded
      in their original audio format.

Enter YouTube URL (or 'q' to quit): https://www.youtube.com/watch?v=dQw4w9WgXcQ

Select download format:
1. MP3 (Audio only)
2. MP4 (Video)

Enter your choice (1 or 2): 1

Downloading as MP3...
Please wait...

✓ Successfully downloaded: Video Title
✓ Saved to: /path/to/downloads

Download another video? (y/n): n

Thank you for using YouTube Downloader!
```

## Notes

- Videos are saved in the `downloads` folder in the current directory
- MP3 conversion requires FFmpeg to be installed on your system
- Without FFmpeg, audio will be downloaded in the original format (usually m4a or webm)
- The tool supports any video from YouTube that yt-dlp can access

## Troubleshooting

**"yt-dlp is not installed" error:**
- Run `pip install yt-dlp` to install the required library

**MP3 conversion fails:**
- Install FFmpeg on your system
- Without FFmpeg, audio will be downloaded in its original format

**Download fails:**
- Check your internet connection
- Verify the YouTube URL is correct and accessible
- Some videos may be restricted or unavailable

## Legal Notice

Please respect copyright laws and YouTube's Terms of Service. This tool is intended for downloading content you have permission to download, such as:
- Your own videos
- Creative Commons licensed content
- Public domain content
- Content where you have explicit permission from the copyright holder

## License

This project is provided as-is for educational purposes.
