import os
import sys
import zipfile
from pathlib import Path

if len(sys.argv) != 3:
    print("Usage: python create_zip.py <source_directory> <zip_file_name>")
    sys.exit(1)

source_directory = sys.argv[1]
zip_file_name = sys.argv[2]



with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    source_path = Path(source_directory)
    for file_path in source_path.rglob('*'):
          archive_path = file_path.relative_to(source_path).as_posix()
          zipf.write(file_path, archive_path)
