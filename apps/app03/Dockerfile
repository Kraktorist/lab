FROM python:3.8-alpine
RUN ["mkdir", "/app"]
WORKDIR /app
VOLUME /db
COPY app.py /app
ENV interval=3
ENV dbpath="/db/app03.db"
CMD ["python", "/app/app.py"]
