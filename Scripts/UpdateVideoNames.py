import os
import re

def get_highest_video_number(folder_path):
    files = os.listdir(folder_path)
    highest_video_number = 0

    for file in files:
        if file.endswith('.mp4'):
            match = re.search(r'video(\d+).mp4', file)
            if match:
                current_video_number = int(match.group(1))
                if current_video_number > highest_video_number:
                    highest_video_number = current_video_number

    return highest_video_number

def rename_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    video_counter = get_highest_video_number(folder_path) + 1

    for file in files:
        # Ensure the file has the .mp4 extension and is not already in the videoX.mp4 format
        if file.endswith('.mp4') and not re.match(r'video(\d+).mp4', file):
            old_file_path = os.path.join(folder_path, file)
            new_file_name = f'video{video_counter}.mp4'
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed {old_file_path} to {new_file_path}')
            
            video_counter += 1

if __name__ == '__main__':
    folder_path = input('Enter the folder path: ')
    rename_files_in_folder(folder_path)
    print('All files have been renamed successfully.')
