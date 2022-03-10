# Use Python 3.9
FROM python:3.9

# Set the working directory for the container to a folder called app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install dependencies
RUN pip install -r requirements.txt

# Start the uwsgi appserver
CMD ["uwsgi", "app.ini"]
