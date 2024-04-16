FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./  # Copies all other project files, including wizexercise.txt

EXPOSE 80 8080 # Port used by Flask's development server

CMD ["python", "app.py"]
