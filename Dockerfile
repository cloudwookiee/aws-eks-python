FROM python:3.13.0b3-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./ 

EXPOSE 80 8080 

CMD ["python", "app.py"]
