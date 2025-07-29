# SafeDownloadDSG

A simple GUI application for downloading YouTube videos using **yt-dlp**.

## Requirements

- Python 3
- `yt-dlp` and `ffmpeg` available in your PATH

## Usage

Run the GUI application with:

```bash
python3 main.py
```

On the **YT-DownloadSafe** tab, paste a YouTube URL and choose one of the available formats:

- **MP4 best** – download the best quality video and audio
- **MP4 1080p** – limit video quality to 1080p if available
- **MP3 audio** – extract audio only as MP3

The tool invokes `yt-dlp` with appropriate options based on the selection.
