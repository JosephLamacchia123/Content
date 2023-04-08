import json
import requests
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    return {
        postToFacebook()
    }
    
    
    
def postToFacebook():
  
    payload = {
      "post": "Today is a great day!",
      "platforms": ["facebook"],
	    "mediaUrls": ["https://img.ayrshare.com/012/gb.jpg"],
      }
logger.info('Payload :: ' + payload)
      
    headers = {'Content-Type': 'application/json', 
    'Authorization': 'Bearer HHSTHH6-MWCMSG4-N2QA5BZ-3MQ2CDH'}
      
    response = requests.post('https://app.ayrshare.com/api/post', 
          json=payload, 
          headers=headers)
	
logger.info('Response :: ' + response)
          
    return response
