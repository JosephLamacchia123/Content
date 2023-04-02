import json
import boto3
import io




def lambda_handler(event, context):
    text = event['text']
    
    return {
        'mp3Location': synthesize_speech(text)
    }
    
    
def synthesize_speech(text, output_format='mp3', voice_id='Joanna'):
    
    polly = boto3.client('polly')
    response = polly.synthesize_speech(Text=text, OutputFormat=output_format, VoiceId=voice_id)

        
    s3 = boto3.client('s3')
    audio_file_key = f"audio/{text[:10]}_{voice_id}.{output_format}"

    with io.BytesIO(response['AudioStream'].read()) as audio_file:
        s3.upload_fileobj(audio_file, 'generated-audio-repository', audio_file_key)

    return audio_file_key
    
    
