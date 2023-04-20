import json
import boto3
import random
import string
import io




def lambda_handler(event, context):

    content = event['TextContent']['content']
    
    title =  event['TextContent']['title']
    ssml = f"<speak><break time='2s'/>{content}<break time='2s'/></speak>"
    return {
        'mp3Location': synthesize_speech(ssml,output_format='mp3',voice_id='Justin')
    }
    
    
    
    
def synthesize_speech(text, output_format, voice_id):
    
    polly = boto3.client('polly')
    response = polly.synthesize_speech(Text=text, TextType='ssml', OutputFormat=output_format, VoiceId=voice_id)

    s3 = boto3.client('s3')
    audio_file_key = 'audio/' + generate_random_string(10) + '.mp3'

    with io.BytesIO(response['AudioStream'].read()) as audio_file:
        s3.upload_fileobj(audio_file, 'generated-audio-repository', audio_file_key)

    return audio_file_key
    
    

def generate_random_string(length):
    # Combine all ASCII letters (both lowercase and uppercase) and digits
    characters = string.ascii_letters + string.digits
    # Generate a random string of the specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

