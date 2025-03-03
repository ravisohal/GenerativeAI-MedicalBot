FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the files to the working directory
COPY . /app/

# Install the dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "app.py"]