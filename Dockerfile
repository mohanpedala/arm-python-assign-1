
FROM python:3.10-slim

WORKDIR /app

COPY ./src /app/src

ENV LOG_FILE_PATH=/app/src/server.log

# RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/app/src/main.py"]