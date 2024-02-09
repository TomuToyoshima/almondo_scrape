FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && \
    apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade wheel

RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y
RUN apt install python3-selenium -y

RUN pip install -r requirements.txt