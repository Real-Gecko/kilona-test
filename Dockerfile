FROM python:3.12-slim

COPY requirements.txt /
RUN --mount=type=cache,target=/root/.cache/pip pip install -r /requirements.txt

RUN useradd -m app
USER app

RUN mkdir ~/app
WORKDIR /home/app/app

COPY . .

EXPOSE 50051

CMD [ "python", "server.py" ]
