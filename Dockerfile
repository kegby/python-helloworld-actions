# Comment: My First Docker File. 
# Build Image For Hello World App From Latest Python Version 

FROM python:latest
LABEL maintainer="kegby"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "app.py" ]