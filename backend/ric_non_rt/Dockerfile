# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Copy the rest of the working directory contents into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5003

# Run the application
CMD ["python", "ric_non_rt.py"]
