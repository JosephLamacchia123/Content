from moviepy.editor import ImageSequenceClip, concatenate_videoclips, ImageClip, TextClip, CompositeVideoClip
from moviepy.video.fx import all
import requests
import textwrap
import boto3

from PIL import Image
import numpy as np
import io

def lambda_handler(event, context):
    parallel_results = event.get('parallelResults', [])

    # Access the 'content' and 'title' keys in the first item of the parallel_results list
    if parallel_results:
        content = parallel_results[0].get('content', '')

    return create_video(event['imageUrls'],'generatedVideo.mp4',30,3,content,event['mp3Location'])

def create_video_from_image_urls(image_urls, output_video, fps, display_duration,text,mp3Location):
    
    #Downloads images and adds to numpy array
      images = []
      for image_url in image_urls:
        response = requests.get(image_url)
        image = Image.open(io.BytesIO(response.content))
        image_np = np.array(image)
        images.append(image_np)
         
      #Turns images into clips of the specified duration and appends them into one video
      clips = []
      for image in images:
            clip = ImageClip(image, duration=display_duration)
            clips.append(clip)
      concatenated_clip = concatenate_videoclips(clips)
    
    #Defines text to be displayed in the video
      wrapped_text = '\n'.join(textwrap.wrap(text, 40))
      text_clip = TextClip(wrapped_text, fontsize=100, color='Yellow',font='Roboto',stroke_color='black', stroke_width=4)
      text_clip = text_clip.set_pos(('center', 'bottom'))
      text_clip = text_clip.set_duration(concatenated_clip.duration)
    
    #Combines video and text into one
      final_clip = CompositeVideoClip([concatenated_clip, text_clip])

      #Add audio to video
      mp3 = getMp3FileFromS3(mp3Location)
      final_clip.set_audio(mp3)
        
    #Creates final video
      final_clip.write_videofile(output_video,fps=30)

def getMp3FileFromS3(s3_key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket='generated-audio-repository', Key=s3_key)
    file_content = response['Body'].read()
    return file_content
