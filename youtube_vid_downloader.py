"""
Author: Ahmed Abdelmotteleb
Last updated: 15 Apr 2024
Script that downloads a YouTube video given its link.
"""

from pytube import YouTube, Stream
from sys import argv

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

def main():
    link = argv[1]
    yt = YouTube(link, on_progress_callback=progress_function)

    print(f'Video title: {yt.title}')

    vid = yt.streams.get_highest_resolution()

    print(f'Resolution: {vid.resolution}')
    vid.download()
    print('\nDownload completed.')

if __name__ == "__main__":
    main()