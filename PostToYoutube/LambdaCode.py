import os
import google_auth_oauthlib.flow
import google.oauth2.credentials
import google_auth_httplib2
import googleapiclient.discovery
import googleapiclient.errors
import boto3
import tempfile

def lambda_handler(event, context):
    # Replace with your S3 bucket and video file details
    BUCKET_NAME = "generated-content1"
    KEY = "output.mp4"
    
    s3 = boto3.client("s3")

    # Download the video file from S3 to a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        s3.download_file(BUCKET_NAME, KEY, temp_file.name)
        
        # Set up the YouTube API client
        youtube = get_authenticated_youtube_client()
        
        # Upload the video to YouTube
        upload_video_to_youtube(youtube, temp_file.name)

def get_authenticated_youtube_client():
    # Set up OAuth 2.0 credentials
    creds = google.oauth2.credentials.Credentials.from_authorized_user_info(
        info={
            "client_id": os.environ["CLIENT_ID"],
            "client_secret": os.environ["CLIENT_SECRET"],
	    "refresh_token": os.environ["REFRESH_TOKEN"],
            "scopes": ["https://www.googleapis.com/auth/youtube.upload"],
            "token_uri": "https://oauth2.googleapis.com/token",
        }
    )

    # Build the YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)
    return youtube

def upload_video_to_youtube(youtube, video_file_path):
    # Set the video metadata
    body = {
        "snippet": {
            "title": "My uploaded video from AWS Lambda",
            "description": "This video was uploaded from an AWS Lambda function.",
            "tags": ["aws", "lambda", "youtube"],
            "categoryId": "22"  # Category ID for "People & Blogs"
        },
        "status": {
            "privacyStatus": "private"  # or "public" or "unlisted"
        }
    }

    # Upload the video file
    with open(video_file_path, "rb") as video_file:
        request = youtube.videos().insert(
            part="snippet,status",
            body=body,
            media_body=googleapiclient.http.MediaFileUpload(video_file_path, chunksize=-1, resumable=True)
        )
        response = request.execute()

    print(f"Video uploaded with video ID: {response['id']}")











