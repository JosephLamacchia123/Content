import json
import requests

def lambda_handler(event, context):
    return {
        'Images': urls
    }
    
    
def generate_images():
    urls = []
    for i in range(3):
        response = requests.get('https://picsum.photos/200/300.jpg')
        url = response.url
        urls.append(url)
    return urls


