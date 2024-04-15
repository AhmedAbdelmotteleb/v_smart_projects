"""
Author: Ahmed Abdelmotteleb
Last updated: 15 Apr 2024
Script that downloads a YouTube video given its link.
"""

from pytube import YouTube, Stream
from sys import argv
from youtube_transcript_api import YouTubeTranscriptApi
import ffmpeg
import datetime


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
    caption = yt.captions.get(language) if language in yt.captions else None
    if caption is not None:
        return caption.generate_srt_captions()

    # If no manually created captions are available, try to download auto-generated captions
    print(f'No manually created captions available in {language}. Trying auto-generated captions...')
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
    except Exception as e:
        print(f'Error downloading auto-generated captions: {e}')
        return ''

    return convert_transcript_to_srt(transcript)


def convert_transcript_to_srt(transcript: list) -> str:
    """
    Convert a transcript to SRT format.

    Args:
        transcript (list): The transcript.

    Returns:
        str: The transcript in SRT format.
    """
    srt = ''
    for i in range(len(transcript)):
        start = transcript[i]['start']

        # If this is not the last entry, make sure the end time doesn't overlap with the next entry
        if i < len(transcript) - 1:
            next_start = transcript[i + 1]['start']
            end = min(start + transcript[i]['duration'], next_start)
        else:
            end = start + transcript[i]['duration']

        # Convert the timestamps to the correct format
        start_sec, start_ms = divmod(start, 1)
        end_sec, end_ms = divmod(end, 1)

        start_hms = str(datetime.timedelta(seconds=int(start_sec)))
        end_hms = str(datetime.timedelta(seconds=int(end_sec)))

        start_srt = f"{start_hms},{int(start_ms*1000):03}"
        end_srt = f"{end_hms},{int(end_ms*1000):03}"

        text = transcript[i]['text']
        srt += f'{i+1}\n{start_srt} --> {end_srt}\n{text}\n\n'
    return srt

def main():
    link = argv[1]
    yt = YouTube(link, on_progress_callback=progress_function)
    vid_file_name = yt.title.replace(' ', '_')

    print(f'Video title: {yt.title}')

    vid = yt.streams.get_highest_resolution()

    print(f'Resolution: {vid.resolution}')
    
    vid.download(filename=vid_file_name + '.mp4')

    # Download captions
    captions = download_captions(yt, yt.video_id)
    caption_file = f'{vid_file_name}_captions.srt'
    with open(caption_file, 'w') as f:
        f.write(captions)

    print('\nDownload completed.')
    
    # Add captions to video
    ffmpeg.input(vid_file_name + '.mp4').output(f'{vid_file_name}_subtitled.mp4', vf="subtitles=" + caption_file).run(overwrite_output=True)

if __name__ == "__main__":
    main()