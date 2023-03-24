FROM python:3

RUN mkdir /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app

run pip install --upgrade pip
run pip install -r requirements.txt

COPY . /app

EXPOSE 3000
CMD python ./main.py
