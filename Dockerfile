FROM python:3.9.7-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]