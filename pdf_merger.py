"""
Author: Ahmed Abdelmotteleb
Last updated: 15 Apr 2024
Script that merges PDF files in a directory.
"""

import PyPDF2
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Merge PDF files in a directory')

    parser.add_argument('--dir', required=True, type=str, help='the directory to merge PDFs from')
    parser.add_argument('--output', required=True, type=str, help='the output file name')
    parser.add_argument('--sort', action='store_true', help='sort the files before merging')
    parser.add_argument('--files', nargs='*', help='specific files to merge')

    args = parser.parse_args()

    if not os.path.exists(args.dir):
        print(f'Directory {args.dir} does not exist.')
        exit(1)

    if os.path.exists(args.output):
        should_overwrite = input(f"File {args.output} already exists. Do you want to overwrite it? (y/n): ")
        if should_overwrite.lower() != 'y':
            print("Exiting without overwriting the file.")
            exit(0)

    merger = PyPDF2.PdfFileMerger()

    files = args.files if args.files else os.listdir(args.dir)
    if args.sort:
        files.sort()

    pdf_files = [file for file in files if file.endswith('.pdf')]

    if not pdf_files:
        print(f"No PDF files found in directory {args.dir}.")
        exit(1)

    for file in pdf_files:
        merger.append(os.path.join(args.dir, file))

    merger.write(args.output)
    merger.close()

if __name__ == "__main__":
    main()