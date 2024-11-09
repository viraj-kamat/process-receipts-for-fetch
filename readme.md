Project Name:
Process Receipts

Description:
Process Receipts is a Python application that provides a simple web server to process receipts via HTTP API

Getting Started:
 Prerequisites
  Docker installed on your system

Building the Docker Image:
 To build the Docker image, run the following command in the root directory of the project:
  docker build -t processreceipt .



Running the Test Cases:
 To run the test cases, use the following command:
  docker run processreceipt python3 -m unittest discover -s tests -p 'test*.py'

Running the Server with Test Cases:
 To run the server with test cases, use the following script:
  ./run_server.sh

This script will build the Docker image, run the test cases, and then start the server if the test cases pass.


Making the API calls:
 Navigate to http://0.0.0.0:8000/docs
 The application utilizes FastAPI, the webpage is self-explanatory to make REST calls to process receipts or fetch points for a rceipt

License:
This project is licensed under the MIT License.

Contributing:
Contributions are welcome! Please submit a pull request with your changes.

Authors:
Viraj Kamat
