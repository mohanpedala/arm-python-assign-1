
FROM python:3.10-slim

COPY ./src .
WORKDIR /app/src

RUN ls -al

# RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]

