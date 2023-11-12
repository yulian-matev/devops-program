FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install -y python3 \
       python3-pip


WORKDIR /opt/devops-programme

# Install requirements
COPY app/requirements.txt .
RUN pip install -r requirements.txt

RUN useradd -ms /bin/bash usr_app
USER usr_app

COPY app .

ARG FLASK_APP_PORT=5000
EXPOSE $FLASK_APP_PORT

#CMD echo hello $(whoami)
CMD python3  /opt/devops-programme/app.py