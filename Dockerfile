# Select a base Python image 
FROM python:3.9-slim  

# Set the working directory within the image
WORKDIR /app

# Copy your project's dependencies file (if you have one)
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy your application code into the working directory
COPY . . 

# Expose the port your Flask app will listen on
EXPOSE 8080 

# Define the command to run your app 
CMD ["python", "app.py"]  
