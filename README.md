# FastAPI Image Upload and Base64 Conversion

This FastAPI application provides endpoints to upload an image and convert it to a base64 string, as well as a health check endpoint.

## Features

- **Upload Image**: Upload an image file and get its base64-encoded string.
- **Health Check**: Check the health status of the application.

## Endpoints

### Health Check

- **URL**: `/healthcheck`
- **Method**: `GET`
- **Response**: 
  ```json
  {
    "status": "ok"
  }
