import requests
from bs4 import BeautifulSoup
import re
import os
from pathlib import Path
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import time


def extract_hyperlinks(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to get URL {url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    comments_section = soup.find('td', class_='tablecell comments mathjax')

    if comments_section:
        print(f'Comments section found on {url}.')
        hyperlinks = [a['href'] for a in comments_section.find_all('a')]
        print(f'Found {len(hyperlinks)} hyperlink(s) in the comments section.')
        print(hyperlinks)
        return hyperlinks
    else:
        print(f'Comments section not found on {url}.')
        return []


def download_external_figures(links, output_folder):
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    with requests.Session() as session:
        for link in links:
            try:
                external_response = session.get(link)
                external_response.raise_for_status()
            except requests.RequestException as e:
                print(f"Failed to get URL {link}: {e}")
                continue

            external_soup = BeautifulSoup(external_response.content, 'html.parser')

            # Create a subdirectory for this URL
            url_path = urlparse(link).path
            url_base = Path(url_path).stem
            url_output_folder = output_folder / url_base
            url_output_folder.mkdir(parents=True, exist_ok=True)

            for img_tag in external_soup.find_all('img', src=True):
                img_url = urljoin(link, img_tag['src'])
                print(f"Found image: {img_url}")

                try:
                    img_response = session.get(img_url)
                    img_response.raise_for_status()
                except requests.RequestException as e:
                    print(f"Failed to get image {img_url}: {e}")
                    continue

                sanitized_filename = re.sub(r'[\\/*?:"<>|]', '_', Path(img_url).name)
                img_filename = url_output_folder / sanitized_filename

                with open(img_filename, 'wb') as img_file:
                    img_file.write(img_response.content)
                print(f"Downloaded: {img_filename}")

if __name__ == "__main__":
    urls = ['https://arxiv.org/abs/2109.01113', 'https://arxiv.org/abs/2305.10515', 'https://arxiv.org/abs/2305.16623']
    output_folder = "output_figures"

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        for url in urls:
            executor.submit(download_external_figures, extract_hyperlinks(url), output_folder)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time} seconds")