# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Upgrade pip to the latest version
RUN python3 -m pip install --upgrade pip

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any necessary dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the working directory contents into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5005

# Run the application
CMD ["python3", "edge_node.py"]
