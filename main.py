import argparse
import yt_dlp
import whisper
import os

def download(url, audio_only=False, quality='best', transcribe=False, cc=False, cc_lang='en', cc_mode=None):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestaudio/best' if audio_only else quality,
        'quiet': False,
        'noplaylist': True,
    }

    if audio_only:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        ydl_opts['merge_output_format'] = 'mp3'
    else:
        ydl_opts['merge_output_format'] = 'mp4'
    
    if cc:
        ydl_opts['writesubtitles'] = True
        ydl_opts['subtitleslangs'] = [cc_lang]
        ydl_opts['subtitlesformat'] = 'vtt'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        output_path = ydl.prepare_filename(info)

# Handle subtitle extraction or burning
    if cc:
        subtitle_file = output_path.rsplit('.', 1)[0] + f".{cc_lang}.vtt"

        if cc_mode == "txt":
            try:
                import webvtt
                text_file = output_path.rsplit('.', 1)[0] + f".{cc_lang}.txt"
                with open(text_file, "w", encoding="utf-8") as f:
                    for caption in webvtt.read(subtitle_file):
                        f.write(caption.text + "\\n")
                print(f"✅ Subtitle text exported to: {text_file}")
            except ImportError:
                print("⚠️ 'webvtt' package is not installed. Run: pip install webvtt-py")

        elif cc_mode == "burn":
            burned_output = output_path.rsplit('.', 1)[0] + f".subtitled.mp4"
            os.system(f'ffmpeg -i "{output_path}" -vf subtitles="{subtitle_file}" "{burned_output}"')
            print(f"✅ Video with burned-in subtitles saved to: {burned_output}")


    if transcribe:
            # If video, convert to mp3 before transcription
        if not audio_only:
            mp3_path = output_path.rsplit('.', 1)[0] + '.mp3'
            os.system(f'ffmpeg -i "{output_path}" -vn -acodec libmp3lame "{mp3_path}"')
        else:
            mp3_path = output_path
        
        model = whisper.load_model("base")
        result = model.transcribe(mp3_path)
        with open("transcription.txt", "w", encoding="utf-8") as f:
            f.write(result["text"])
        print("✅ Transcription saved to transcription.txt")


        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube videos or audio using yt-dlp.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--audio", action="store_true", help="Download audio only (MP3)")
    parser.add_argument("--quality", default="best", help="Video quality format (default: best)")
    parser.add_argument("--transcribe", action="store_true", help="Transcribe audio to text")
    parser.add_argument("--cc", action="store_true", help="Download closed captions (if available)")
    parser.add_argument("--cc-lang", default="en", help="Language code for subtitles (default: en)")
    parser.add_argument("--cc-mode", choices=["txt", "burn"], help="What to do with subtitles: txt = export, burn = embed")

    args = parser.parse_args()
    download(
        args.url,
        audio_only=args.audio,
        quality=args.quality,
        transcribe=args.transcribe,
        cc=args.cc,
        cc_lang=args.cc_lang,
        cc_mode=args.cc_mode
        )
