import os
import json
import openai


def lambda_handler(event, context):
    prompt = event['prompt']
    generated_text = generate_text(prompt)
    generated_title = generate_text('Write a title for a post with the following content' + generated_text)
    return {
        'content': generated_text,
        'title': generated_title
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
    
