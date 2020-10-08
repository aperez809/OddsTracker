FROM python:3.7
ENV PYTHONUNBUFFERED 1

# create root directory for project in the container
RUN mkdir /odds

# Set the working directory to /container_odds
WORKDIR /odds

# Copy the current directory contents into the container at /container_odds
ADD . /odds

# Install any needed packages specified in requirements.txt
RUN pip install pipenv
COPY Pipfile Pipfile.lock /odds/
RUN pipenv install --system

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000", "--settings=oddstracker_admin.settings_testing"]