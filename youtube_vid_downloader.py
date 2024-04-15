"""
Author: Ahmed Abdelmotteleb
Last updated: 15 Apr 2024
Script that downloads a YouTube video given its link.
"""

from pytube import YouTube, Stream
from sys import argv
from youtube_transcript_api import YouTubeTranscriptApi

def progress_function(stream: Stream, chunk: bytes, bytes_remaining: int) -> None:
    """
    Callback function that shows the download progress.

    Args:
        stream (Stream): The stream that is being downloaded.
        chunk (bytes): The data that has just been downloaded.
        bytes_remaining (int): The number of bytes left to download.
    """
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    live_progress = (bytes_downloaded / total_size) * 100
    print(f'Downloading... {live_progress:.1f}%', end='\r')


def download_captions(yt: YouTube, video_id: str, language: str = 'en') -> str:
    """
    Download captions for a YouTube video.

    Args:
        yt (YouTube): The YouTube video.
        video_id (str): The ID of the YouTube video.
        language (str): The language code for the captions (default is 'en' for English).

    Returns:
        str: The captions as a string, or an empty string if no captions are available.
    """
    # Try to download manually created captions
    caption = yt.captions.get_by_language_code(language)
    if caption is not None:
        return caption.generate_srt_captions()

    # If no manually created captions are available, try to download auto-generated captions
    print(f'No manually created captions available in {language}. Trying auto-generated captions...')
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
    except Exception as e:
        print(f'Error downloading auto-generated captions: {e}')
        return ''

    # Convert the transcript to SRT format
    srt = ''
    for i, entry in enumerate(transcript):
        start = entry['start']
        duration = entry['duration']
        end = start + duration
        text = entry['text']
        srt += f'{i+1}\n{start} --> {end}\n{text}\n\n'
    return srt

def main():
    link = argv[1]
    yt = YouTube(link, on_progress_callback=progress_function)

    print(f'Video title: {yt.title}')

    vid = yt.streams.get_highest_resolution()

    print(f'Resolution: {vid.resolution}')
    vid.download()

    # Download captions
    captions = download_captions(yt, yt.video_id)
    caption_file = f'{yt.title}_captions.srt'
    with open(caption_file, 'w') as f:
        f.write(captions)

    print('\nDownload completed.')

if __name__ == "__main__":
    main()