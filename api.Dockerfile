FROM python:3.6-slim-buster

WORKDIR /api

COPY ./api .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py", "--host=0.0.0.0", "--port=5000"]