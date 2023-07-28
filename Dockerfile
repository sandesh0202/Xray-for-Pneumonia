# Start from Amazon Linux image
FROM amazonlinux:2

# Install Python and other dependencies
RUN amazon-linux-extras enable python3
RUN yum install -y python3 awscli

WORKDIR /app

COPY . /app
RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py" ]
