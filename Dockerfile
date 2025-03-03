FROM python:3.7-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the files to the working directory
COPY . /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]