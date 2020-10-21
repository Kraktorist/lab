FROM python:3.8-alpine
RUN ["mkdir", "/app"]
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "-u", "/app/app.py"]
