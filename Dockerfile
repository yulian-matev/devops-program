FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install -y python3 \
       python3-pip


WORKDIR /opt/devops-programme

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN useradd -ms /bin/bash usr_app
USER usr_app

COPY app .

EXPOSE 5000
#CMD echo hello $(whoami)
CMD python3  /opt/devops-programme/app.py