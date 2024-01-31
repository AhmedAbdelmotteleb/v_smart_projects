"""
Author: Ahmed Abdelmotteleb
Last updated: 12 Dec 2023
Script that organises the a directory by moving files into folders based on their extension.
"""

import os
import shutil
import argparse
import json
import datetime

def create_folders_if_not_exist(directory_path, extension_folders):
    """
    Create folders in the specified directory for each file extension.

    Parameters:
    directory_path (str): The path to the directory where the folders should be created.
    extension_folders (dict): A dictionary mapping file extensions to folder names.
    """
    for folder in extension_folders.values():
        os.makedirs(os.path.join(directory_path, folder), exist_ok=True)

def organize_files_by_extension(directory_path, extension_folders):
    """
    Organize the files in the specified directory by their extension.

    Files are moved into the corresponding folder for their extension, as specified by the extension_folders dictionary.
    A report of the moved files is returned.

    Parameters:
    directory_path (str): The path to the directory to organize.
    extension_folders (dict): A dictionary mapping file extensions to folder names.

    Returns:
    report (dict): A dictionary of strings describing the moved files.
    """

    report = {}
    file_count = 0
    for file_name in os.listdir(directory_path):
        # Ignore directories, only process files
        if not os.path.isdir(os.path.join(directory_path, file_name)):
            file_extension = os.path.splitext(file_name)[1]

            if file_extension in extension_folders:
                file_count += 1
                destination_folder = os.path.join(directory_path, extension_folders[file_extension])
                file_path = os.path.join(directory_path, file_name)
                new_file_path = os.path.join(destination_folder, file_name)

                if os.path.exists(new_file_path):
                    # File already exists at the destination, skip it and add a note to the report
                    report[file_count] = {"file_name": file_name, "status": "Skipped (file already exists at the destination)"}
                else:
                    shutil.move(file_path, destination_folder)
                    # Add the file and its new location to the report
                    report[file_count] = {"file_name": file_name, "new_location": destination_folder, "status": "Moved"}

    # Return the report
    return report

def main():
    parser = argparse.ArgumentParser(description='Organize directory by file extension.')
    parser.add_argument('--directory', type=str, help='The directory to organize (default is Windows Desktop).', default=os.path.join(os.path.expanduser('~'), 'Desktop'))
    parser.add_argument('--log', action='store_true', help='Whether or not to output JSON file report log.', default=False)
    args = parser.parse_args()

    # Check if the directory exists
    if not os.path.isdir(args.directory):
        raise ValueError(f"Invalid directory path: {args.directory}")

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

    create_folders_if_not_exist(args.directory, extension_folders)
    report = organize_files_by_extension(args.directory, extension_folders)

    if not report:
        print("No files were moved.")
        return
    else:
        for i, entry in enumerate(report.values()):
            print(f"{i + 1}. {entry['file_name']}: {entry['status']}")
    
    if report and args.log:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(os.path.join(args.directory, f'report_{current_time}.json'), 'w') as f:
            json.dump(report, f, indent=4)

if __name__ == "__main__":
    main()
