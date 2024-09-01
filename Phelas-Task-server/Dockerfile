FROM python:3.11

WORKDIR /server

COPY ./requirements.txt /server/requirements.txt

RUN pip install -r /server/requirements.txt

COPY main.py /server/main.py

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "80"]
