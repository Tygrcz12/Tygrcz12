# YouTube Video/Audio Downloader

A simple command-line tool to download videos from YouTube in MP3 (audio) or MP4 (video) format.

## Features

- Download YouTube videos in MP4 format with quality selection
- **High resolution support**: Choose from Best/1080p/720p/480p/360p
- Extract audio and save as MP3 format
- User-friendly command-line interface
- Downloads saved to a dedicated 'downloads' folder
- Simple URL input and format selection

## Requirements

- Python 3.6 or higher
- yt-dlp library (installed via requirements.txt)
- **FFmpeg (STRONGLY RECOMMENDED)**

### Why FFmpeg is Important

FFmpeg is required for:
- **MP3 conversion**: Converting audio to MP3 format (without it, audio downloads in original format like m4a/webm)
- **High-quality video**: Merging separate video and audio streams for best quality
- **Format conversion**: Converting between different video formats

**The downloader will work without FFmpeg, but with limited functionality.** You'll see warnings and get lower quality results.

## Installation

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Install FFmpeg (STRONGLY RECOMMENDED):**
   - **Windows**: 
     1. Download from [ffmpeg.org](https://ffmpeg.org/download.html)
     2. Extract the archive
     3. Add the `bin` folder to your system PATH
     4. Verify: `ffmpeg -version`
   
   - **Linux (Debian/Ubuntu)**: 
     ```bash
     sudo apt-get update
     sudo apt-get install ffmpeg
     ```
   
   - **macOS**: 
     ```bash
     brew install ffmpeg
     ```
   
   - Verify installation: Run `ffmpeg -version` in your terminal

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
   - If you selected MP4, choose video quality:
     - `1` for Best available (highest quality)
     - `2` for 1080p (Full HD)
     - `3` for 720p (HD)
     - `4` for 480p (SD)
     - `5` for 360p (Low)
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

Enter your choice (1 or 2): 2

Select video quality:
1. Best available (highest quality)
2. 1080p (Full HD)
3. 720p (HD)
4. 480p (SD)
5. 360p (Low)

Enter your choice (1-5): 3

Downloading as MP4...
Quality: 720p
Please wait...

✓ Successfully downloaded: Video Title
✓ Saved to: /path/to/downloads

Download another video? (y/n): n

Thank you for using YouTube Downloader!
```

## Notes

- Videos are saved in the `downloads` folder in the current directory
- **FFmpeg is strongly recommended** for full functionality
- Without FFmpeg:
  - Audio will download in original format (m4a/webm) instead of MP3
  - Videos may download in lower quality (single-file format only)
  - High-quality downloads that require merging video+audio will fail
- The tool detects FFmpeg automatically and adapts functionality
- **Quality selection**: When selecting a specific resolution (e.g., 720p), the tool will download that quality or the next best available if the exact resolution is not available
- **Best quality option**: Selecting "Best available" will download the highest quality version (requires FFmpeg for best results)

## Troubleshooting

**"yt-dlp is not installed" error:**
- Run `pip install yt-dlp` to install the required library

**"ERROR: You have requested merging of multiple formats but ffmpeg is not installed":**
- This means FFmpeg is required but not found
- Install FFmpeg following the instructions above
- The tool will now automatically handle this by downloading single-file formats when FFmpeg is missing

**MP3 conversion fails or downloads in wrong format:**
- Install FFmpeg on your system
- Verify FFmpeg is in your PATH by running: `ffmpeg -version`
- Without FFmpeg, audio will be downloaded in its original format (m4a/webm)

**"No supported JavaScript runtime" warning:**
- This is a yt-dlp warning that can usually be ignored
- For some videos, you may need to install `deno` runtime
- Most videos work fine without it

**Download fails:**
- Check your internet connection
- Verify the YouTube URL is correct and accessible
- Some videos may be restricted or unavailable
- Try a different quality/format option

## Legal Notice

Please respect copyright laws and YouTube's Terms of Service. This tool is intended for downloading content you have permission to download, such as:
- Your own videos
- Creative Commons licensed content
- Public domain content
- Content where you have explicit permission from the copyright holder

## License

This project is provided as-is for educational purposes.
