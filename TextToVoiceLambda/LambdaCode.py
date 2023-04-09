import json
import boto3
import random
import string
import io




def lambda_handler(event, context):
    parallel_results = event.get('parallelResults', [])

    # Access the 'content' and 'title' keys in the first item of the parallel_results list
    
    content = parallel_results[0].get('content', '')
    title = parallel_results[0].get('title', '')
    
    return {
        'mp3Location': synthesize_speech(content)
    }
    
    
def synthesize_speech(text, output_format='mp3', voice_id='Joanna'):
    
    polly = boto3.client('polly')
    response = polly.synthesize_speech(Text=text, OutputFormat=output_format, VoiceId=voice_id)

        
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

