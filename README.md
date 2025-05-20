# panel-agent

# TODO: update README

A simple CLI tool to download your own YouTube videos or audio using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).

## ✅ Features

- Download video or audio (MP3)
- Specify quality (e.g., best, 720p)
- Command-line interface
- Specify subtitle language
- Transcribe audio using [Whisper](https://github.com/openai/whisper)
- Burn subtitles using [FFmpeg](https://ffmpeg.org/)


## 🔧 Requirements

- Python 3.8+
- `yt-dlp`
- `ffmpeg` (for audio extraction)

## 📦 Installation

```bash
git clone https://github.com/your-username/yt_downloader.git
cd yt_downloader
pip install -r requirements.txt
```

Make sure `ffmpeg` is installed and accessible from your `PATH`.

## 🚀 Quick Start

### Download a video (best quality):
```bash
python main.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Download audio only:
```bash
python main.py "https://www.youtube.com/watch?v=VIDEO_ID" --audio
```

### Specify video quality:
```bash
python main.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality "bestvideo[height<=720]+bestaudio"
```

## 📁 Output

- Video: saved as `.mp4`
- Audio: saved as `.mp3`
- Transcribed audio: saved as `.mp3`
- Subtitles: saved as `.vtt`

## ⚠️ License

Use responsibly. You must own the content you're downloading.
