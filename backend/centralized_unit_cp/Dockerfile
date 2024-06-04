# Use a base image with the desired operating system and runtime environment
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files into the container
COPY cu_cp.py .

# Install any required Python packages
RUN pip install some-package another-package

# Expose any ports needed for communication (if applicable)
# EXPOSE 8080

# Command to run the microservice when the container starts
CMD ["python", "cu_cp.py"]
