import yt_dlp
import os
import whisper

def download(url, audio_only=False, quality='best', transcribe=False,
             cc=False, cc_lang='en', cc_mode=None):
    """
    Download YouTube video/audio, extract subtitles or transcription.
    Returns path to media file or transcript.
    """
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestaudio/best' if audio_only else quality,
        'quiet': False,
        'noplaylist': True,
    }

    # Audio/video format
    if audio_only:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        ydl_opts['merge_output_format'] = 'mp3'
    else:
        ydl_opts['merge_output_format'] = 'mp4'

    # Closed captions
    if cc:
        ydl_opts['writesubtitles'] = True
        ydl_opts['subtitleslangs'] = [cc_lang]
        ydl_opts['subtitlesformat'] = 'vtt'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        output_path = ydl.prepare_filename(info)

    # Process captions
    if cc:
        subtitle_file = output_path.rsplit('.', 1)[0] + f".{cc_lang}.vtt"
        if cc_mode == 'txt':
            try:
                import webvtt
                text_file = output_path.rsplit('.', 1)[0] + f".{cc_lang}.txt"
                with open(text_file, 'w', encoding='utf-8') as f:
                    for caption in webvtt.read(subtitle_file):
                        f.write(caption.text + '\n')
                print(f"✅ Subtitle text exported to: {text_file}")
            except ImportError:
                print("⚠️ webvtt not installed; run: pip install webvtt-py")
        elif cc_mode == 'burn':
            burned = output_path.rsplit('artifact/video', 1)[0] + '.subtitled.mp4'
            os.system(f'ffmpeg -i "{output_path}" -vf subtitles="{subtitle_file}" "{burned}"')
            print(f"✅ Video with embedded subtitles saved to: {burned}")

    # Whisper transcription
    if transcribe:
        if not audio_only:
            mp3 = output_path.rsplit('artifact/audio', 1)[0] + '.mp3'
            os.system(f'ffmpeg -i "{output_path}" -vn -acodec libmp3lame "{mp3}"')
        else:
            mp3 = output_path
        model = whisper.load_model('base')
        result = model.transcribe(mp3)
        transcript = output_path.rsplit('artifact/transcript', 1)[0] + '_transcript.txt'
        with open(transcript, 'w', encoding='utf-8') as f:
            f.write(result['text'])
        print(f"✅ Transcription saved to: {transcript}")
        return transcript

    return output_path

download('', transcribe=True)