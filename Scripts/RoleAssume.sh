#!/bin/bash

# Check if the required arguments are provided
if [ "$#" -ne 2 ]; then
  echo "Usage: ./assume_role.sh <access_key> <secret_access_key>"
  exit 1
fi

# Set the input arguments
ACCESS_KEY=$1
SECRET_ACCESS_KEY=$2
ROLE_ARN="arn:aws:iam::529558902673:role/Jason_Developer"

# Configure AWS CLI with the provided access key and secret access key
aws configure set aws_access_key_id $ACCESS_KEY
aws configure set aws_secret_access_key $SECRET_ACCESS_KEY

# Assume the role and save the returned credentials
CREDENTIALS=$(aws sts assume-role --role-arn $ROLE_ARN --role-session-name session1)

# Parse the returned credentials
NEW_ACCESS_KEY=$(echo $CREDENTIALS | jq -r '.Credentials.AccessKeyId')
NEW_SECRET_ACCESS_KEY=$(echo $CREDENTIALS | jq -r '.Credentials.SecretAccessKey')
SESSION_TOKEN=$(echo $CREDENTIALS | jq -r '.Credentials.SessionToken')

# Configure AWS CLI with the new access key, secret access key, and session token
aws configure set aws_access_key_id $NEW_ACCESS_KEY
aws configure set aws_secret_access_key $NEW_SECRET_ACCESS_KEY
aws configure set aws_session_token $SESSION_TOKEN

echo "Successfully assumed role and reconfigured AWS CLI"