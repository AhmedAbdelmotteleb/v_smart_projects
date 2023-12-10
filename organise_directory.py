"""
Author: Ahmed Abdelmotteleb
Last updated: 12 Dec 2023
Script that organises the a directory by moving files into folders based on their extension.
"""

import os
import shutil

def create_folders_if_not_exist(directory_path, extension_folders):
    for folder in extension_folders.values():
        os.makedirs(os.path.join(directory_path, folder), exist_ok=True)

def organize_files_by_extension(directory_path, extension_folders):
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file)
            if extension in extension_folders:
                destination_folder = os.path.join(directory_path, extension_folders[extension])
                shutil.move(file_path, destination_folder)

def main():
    # Path to the desktop (change this to whatever path you want to organize)
    directory_path = os.path.join(os.path.expanduser('~'), 'Desktop')

    # Dictionary of file extensions and their corresponding folder names
    # You can add more extensions and folder names to this dictionary
    extension_folders = {
        '.txt': 'Text Files',
        '.docx': 'Word Documents',
        '.xlsx': 'Excel Files',
        '.jpg': 'Images',
        '.png': 'Images',
        '.PNG': 'Images',
        '.pdf': 'PDFs',
        '.py': 'Python Scripts',
    }

    create_folders_if_not_exist(directory_path, extension_folders)
    organize_files_by_extension(directory_path, extension_folders)

if __name__ == "__main__":
    main()
