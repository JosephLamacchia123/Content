import os
import subprocess
import boto3
import json
import random

def lambda_handler(event, context):

    print_directory_contents('/opt/bin/')
    random_number = random.randint(1, 14)
    # Set the path for the FFmpeg binary
    ffmpeg_path = '/opt/bin/ffmpeg'

    # Set the paths for the input and output files
    input_video = '/tmp/video.mp4'
    input_audio = '/tmp/audio.mp3'
    output_video = '/tmp/output.mp4'

    # Download the input files from S3
    s3 = boto3.client('s3')
    s3.download_file('content-generator-videos', f"video{random_number}.mp4", input_video)
    s3.download_file('generated-audio-repository', event['Speech']['mp3Location'], input_audio)



    ffmpeg_command = [
        ffmpeg_path, '-i', input_video, '-i', input_audio,
        '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental',
        '-map', '0:v:0', '-map', '1:a:0', '-shortest', output_video, '-y'
    ]





    print("Executing FFmpeg command:", ffmpeg_command)

    result = subprocess.run( ffmpeg_command, text=True, capture_output=True)


    if result.returncode != 0:
        print(f"Error occurred during FFmpeg execution:\nCommand: {' '.join(ffmpeg_command)}\nReturn code: {result.returncode}\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}")
        raise Exception("FFmpeg command returned non-zero exit status.")


    # Upload the output file to S3
    s3.upload_file(output_video, 'generated-content1', 'output.mp4')


def print_directory_contents(directory):
    print(f"Contents of {directory}:")
    with os.scandir(directory) as entries:
        for entry in entries:
            print(f"- {entry.name}")


    return {
        'videoLocation':'output.mp4'
    }
