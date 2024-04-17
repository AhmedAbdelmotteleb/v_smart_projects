"""
Author: Ahmed Abdelmotteleb
Last updated: 15 Apr 2024
Script that merges PDF files in a directory.
"""

from PyPDF2 import PdfMerger
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description='Merge PDF files in a directory')

    parser.add_argument('--files-dir', default='.', type=str, help='the directory to merge PDFs from')
    parser.add_argument('--output-dir', default='.', type=str, help='the directory to save the merged PDF')
    parser.add_argument('--output', required=True, type=str, help='the output file name')
    parser.add_argument('--sort', action='store_true', help='sort the files before merging')
    parser.add_argument('--files', nargs='*', help='specific files to merge')

    args = parser.parse_args()

    if not args.output.endswith('.pdf'):
        raise ValueError('Output file must be a PDF file. Use the .pdf extension.')

    if not os.path.exists(args.files_dir):
        raise FileNotFoundError(f'Directory {args.files_dir} does not exist.')
    
    os.makedirs(args.output_dir, exist_ok=True)

    output_file_path = os.path.join(args.output_dir, args.output)
    if os.path.exists(output_file_path):
        should_overwrite = input(f"File {output_file_path} already exists. Do you want to overwrite it? (y/n): ")
        if should_overwrite.lower() != 'y':
            print("Exiting without overwriting the file.")
            sys.exit(0)

    merger = PdfMerger()

    files = args.files if args.files else os.listdir(args.files_dir)
    if args.sort:
        files.sort()

    pdf_files = [file for file in files if file.endswith('.pdf')]

    if not pdf_files:
        raise FileNotFoundError(f"No PDF files found in directory {args.files_dir}.")

    for file in pdf_files:
        merger.append(os.path.join(args.files_dir, file))
        
    print('Merging PDF files...')
    merger.write(output_file_path)
    merger.close()

if __name__ == "__main__":
    main()