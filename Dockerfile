FROM python:3.7
ENV PYTHONUNBUFFERED 1

# create root directory for project in the container
RUN mkdir /container_odds

# Set the working directory to /container_odds
WORKDIR /container_odds

# Copy the current directory contents into the container at /container_odds
ADD . /container_odds/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
