FROM python:3.8.10-buster

WORKDIR /app

COPY ../docker/requirements.txt requirements.txt

RUN pip install --no-cache --user -r requirements.txt

COPY .. .

EXPOSE 5000

CMD ["python3", "-m" , "flask", "db", "upgrade"]
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]