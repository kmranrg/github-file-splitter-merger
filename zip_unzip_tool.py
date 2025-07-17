import os
import argparse
import zipfile

def zip_file_or_dir(source_path, zip_path):
    """Zip a file or directory into `zip_path`."""
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isdir(source_path):
            for root, _, files in os.walk(source_path):
                for file in files:
                    abs_path = os.path.join(root, file)
                    arcname = os.path.relpath(abs_path, start=source_path)
                    zipf.write(abs_path, arcname)
        else:
            zipf.write(source_path, os.path.basename(source_path))
    print(f"Zipped '{source_path}' to '{zip_path}'")

def unzip_file(zip_path, extract_to):
    """Unzip `zip_path` into the folder `extract_to`."""
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f"Extracted '{zip_path}' to '{extract_to}'")

def main():
    parser = argparse.ArgumentParser(description="Zip or unzip files/directories")
    subparsers = parser.add_subparsers(dest='command')

    # zip command
    zip_parser = subparsers.add_parser('zip', help='Create a zip file')
    zip_parser.add_argument('source', help='File or directory to zip')
    zip_parser.add_argument('--output', help='Output zip filename', required=False)

    # unzip command
    unzip_parser = subparsers.add_parser('unzip', help='Extract a zip file')
    unzip_parser.add_argument('zipfile', help='Zip file to extract')
    unzip_parser.add_argument('--output', help='Directory to extract to', default='.')

    args = parser.parse_args()

    if args.command == 'zip':
        zip_name = args.output or (args.source.rstrip(os.sep) + '.zip')
        zip_file_or_dir(args.source, zip_name)
    elif args.command == 'unzip':
        unzip_file(args.zipfile, args.output)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()