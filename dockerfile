FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y software-properties-common vim \
    && add-apt-repository ppa:jonathonf/python-3.6 \
    && apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv \
    && apt-get install -y git

# Update pip
RUN python3.6 -m pip install pip --upgrade && python3.6 -m pip install wheel

RUN pip install Flask
CMD ["python3.6"]
