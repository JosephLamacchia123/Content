import os
import json
import openai


def lambda_handler(event, context):
    prompt = event['prompt']
    generated_text = generate_text(prompt)
    generated_summary_of_text = 'A Very Unsure Man' 
    image = generate_image(generated_summary_of_text)
    return {
        'text': generated_text,
        'images': image
    }
     

openai.api_key = os.environ['OpenAiKey']

def generate_text(prompt, model="text-davinci-002", max_tokens=1000):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.8,
    )
    return response.choices[0].text.strip()
    
def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    image_url = response['data']

    return image_url
