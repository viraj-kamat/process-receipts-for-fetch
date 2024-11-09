#!/bin/bash

# Build the Docker image
docker build -t processreceipt .

# Run the test cases
docker run processreceipt python3 -m unittest discover -s tests -p 'test*.py'

# If the tests pass, run the server
if [ $? -eq 0 ]; then
  docker run -p 8000:8000 processreceipt python3 main.py
else
  echo "Tests failed"
fi