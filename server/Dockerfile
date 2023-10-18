FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install -r client/requirements.txt
RUN pip install -r server/requirements.txt

EXPOSE 50051

CMD ["bash", "-c", "python server/server.py & python client/client.py"]
