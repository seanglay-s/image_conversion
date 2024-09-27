from fastapi import FastAPI, File, UploadFile
import base64
import sys
import logging

app = FastAPI()

# Custom JSON formatter for logging
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "processName": record.processName,
            "process": record.process,
            "threadName": record.threadName,
            "thread": record.thread,
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
        }
        return json.dumps(log_record)

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
json_formatter = JsonFormatter()
stream_handler.setFormatter(json_formatter)
logger.addHandler(stream_handler)

def image_to_base64(image_file):
    logger.debug("Converting image to base64")
    encoded_string = base64.b64encode(image_file.read())
    logger.debug("Image successfully converted to base64")
    return encoded_string.decode('utf-8')

@app.get("/healthcheck")
async def healthcheck():
    logger.info("Healthcheck endpoint was called")
    return {"status": "ok"}

@app.post("/upload-image/")
async def upload_image(file: UploadFile):
    logger.info(f"Received file upload request: {file.filename}")
    try:
        base64_string = image_to_base64(file.file)
        logger.info(f"File {file.filename} successfully processed")
        return {"filename": file.filename, "base64_string": base64_string}
    except Exception as e:
        logger.error(f"Error processing file {file.filename}: {e}")
        return {"error": "Failed to process the image"}, 500