# Use the official Python 3.8 image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the cu_cp.py file into the container at /app
COPY cu_cp.py .

# Optionally expose any ports needed for communication between containers (uncomment if necessary)
EXPOSE 5000

# Run cu_cp.py when the container launches
CMD ["python", "cu_cp.py"]
