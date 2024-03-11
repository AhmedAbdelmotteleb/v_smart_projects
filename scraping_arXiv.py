"""
Author: Ahmed Abdelmotteleb
Last updated: 11 Mar 2024
Script that downloads figures from arXiv URLs.
"""

import requests
from bs4 import BeautifulSoup
import re
import os
from pathlib import Path
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import time
import argparse

def extract_hyperlinks(url: str) -> list[str]:
    """
    Extracts hyperlinks from the comments section of a given arXiv URL.

    Args:
        url (str): The arXiv URL to extract hyperlink(s) from.

    Returns:
        list[str]: A list of hyperlinks found in the comments section. 
        If no comments section is found, returns an empty list.
    """
    try:
        #get the content of the URL
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to get URL {url}: {e}")
        return []

    # Parse the content of the URL
    soup = BeautifulSoup(response.content, 'html.parser')
    # Try to find the comments section in the parsed content (this is unique to arXiv URLs)
    comments_section = soup.find('td', class_='tablecell comments mathjax')

    if comments_section:
        print(f'Comments section found on {url}.')
        # Extract all hyperlinks from the comments section
        hyperlinks = [a['href'] for a in comments_section.find_all('a')]
        print(f'Found {len(hyperlinks)} hyperlink(s) in the comments section.')
        print(hyperlinks)
        return hyperlinks
    else:
        print(f'Comments section not found on {url}.')
        return []


def download_external_figures(links: list[str], output_folder: str) -> None:
    """
    Extracts hyperlinks from the comments section of a given URL.

    Args:
        url (str): The URL to extract hyperlinks from.

    Returns:
        List[str]: A list of hyperlinks found in the comments section. 
        If no comments section is found, returns an empty list.
    """
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    # Start a new session for making HTTP requests
    with requests.Session() as session:
        for link in links:
            try:
                external_response = session.get(link)
                external_response.raise_for_status()
            except requests.RequestException as e:
                print(f"Failed to get URL {link}: {e}")
                continue

            # Parse the content of the link
            external_soup = BeautifulSoup(external_response.content, 'html.parser')

            # Create a subdirectory for this URL
            url_path = urlparse(link).path
            url_base = Path(url_path).stem
            url_output_folder = output_folder / url_base
            url_output_folder.mkdir(parents=True, exist_ok=True)

            for img_tag in external_soup.find_all('img', src=True):
                # Construct the full URL of the image
                img_url = urljoin(link, img_tag['src'])
                print(f"Found image: {img_url}")

                try:
                    img_response = session.get(img_url)
                    img_response.raise_for_status()
                except requests.RequestException as e:
                    print(f"Failed to get image {img_url}: {e}")
                    continue
                
                # Get rid of any characters that might be problematic in a filename
                sanitized_filename = re.sub(r'[\\/*?:"<>|]', '_', Path(img_url).name)
                img_filename = url_output_folder / sanitized_filename

                if img_filename.exists():
                    print(f"Image already exists, skipping: {img_filename}")
                    continue

                with open(img_filename, 'wb') as img_file:
                    img_file.write(img_response.content)
                print(f"Downloaded: {img_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download figures from arXiv URLs.")
    parser.add_argument('-u','--urls', nargs='*', default=['https://arxiv.org/abs/2109.01113'], help="List of URLs to download images from.")    
    parser.add_argument('-o', '--output', type=str, default="arXiv_figures", help="Output folder to save figures.")
    parser.add_argument('-t', '--threads', type=int, default=os.cpu_count(), help="Number of threads to use.")
    args = parser.parse_args()

    output_folder = Path(args.output)
    output_folder.mkdir(parents=True, exist_ok=True)

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for url in args.urls:
            executor.submit(download_external_figures, extract_hyperlinks(url), output_folder)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time} seconds")