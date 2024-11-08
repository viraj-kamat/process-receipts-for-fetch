FROM debian:stable-slim

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy the requirements.txt file
COPY requirements.txt /tmp/requirements.txt


# Install the Python packages listed in requirements.txt
RUN pip3 install -r /tmp/requirements.txt --break-system-packages

# Copy the files to the image
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Expose port 8000
EXPOSE 8000


