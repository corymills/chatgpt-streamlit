# Use the official Python base image based on CentOS 7
FROM centos:7

# Set the working directory in the container
WORKDIR /app

# Install necessary dependencies
RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install python3.11 && \
    yum clean all

# Copy the application code into the container
COPY . .

# Install the required dependencies
RUN pip3 install --upgrade pip \
   && pip3 install poetry \
   && poetry install

# Expose the port that the application listens on
EXPOSE 8501

# Define the command to run the application
CMD ["streamlit", "run", "--server.port=8501", "chatgpt_app_with_api.py"]