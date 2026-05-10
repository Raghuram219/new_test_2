#!/bin/bash

set -e

APP_NAME=myapp

AWS_REGION=ap-south-1
AWS_ACCOUNT_ID=662905738256
ECR_REPOSITORY=myecr1
IMAGE_TAG=v1

REPOSITORY_URI=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY
IMAGE=$REPOSITORY_URI:$IMAGE_TAG

echo "Logging into ECR..."

aws ecr get-login-password --region $AWS_REGION \
| docker login --username AWS --password-stdin $REPOSITORY_URI

echo "Stopping old container..."
docker stop $APP_NAME || true
docker rm $APP_NAME || true

echo "Pulling latest image..."
docker pull $IMAGE

echo "Running new container..."
docker run -d \
  --name $APP_NAME \
  -p 80:8000 \
  $IMAGE

echo "Deployment completed successfully"