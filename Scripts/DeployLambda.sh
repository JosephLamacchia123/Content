#!/bin/bash


# Check if the required arguments are provided
if [ "$#" -ne 3 ]; then
  echo "Usage: ./deploy_lambda.sh <folder_path> <lambda_name>"
  exit 1
fi

# Set the input arguments
FOLDER_PATH=$1
LAMBDA_NAME=$2

# Navigate to the folder containing LambdaCode.py and requirements.txt
cd $FOLDER_PATH

rm -rf venv
# Create a virtual python environment
python -m venv venv

# Activate the virtual environment
source venv/Scripts/activate


# Create a temporary directory for packaging the dependencies and code
mkdir package

# Install the dependencies into the package directory
python -m pip install -r requirements.txt --no-user -t package


# Copy the LambdaCode.py into the package directory
cp LambdaCode.py package



echo "Look here young man"
cd package 
ls 
cd ../




echo "Creating deployment package zip file..."
python ../../Scripts/Zip.py package deployment_package.zip


echo "Uploading deployment package to S3..."
aws s3 cp deployment_package.zip s3://lambda-deployment-packages-storage12/deployment_package.zip

echo "Updating Lambda function with new deployment package..."
aws lambda update-function-code --function-name $LAMBDA_NAME --s3-bucket lambda-deployment-packages-storage12 --s3-key deployment_package.zip



# Deactivate the virtual environment
deactivate

echo "Cleaning up temporary files..."
rm -rf package
rm deployment_package.zip
rm -rf venv

echo "Deployment complete!"






