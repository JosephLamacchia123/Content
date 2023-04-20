#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: ./upload_to_s3.sh <folder_path> <bucket_name>"
    exit 1
fi

folder_path="$1"
bucket_name="$2"

for file in "$folder_path"/*; do
    if [ -f "$file" ]; then
        aws s3 cp "$file" "s3://$bucket_name/$(basename "$file")"
        echo "Uploaded $file to s3://$bucket_name/$(basename "$file")"
    fi
done

echo "All files have been uploaded successfully."
