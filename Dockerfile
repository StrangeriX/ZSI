FROM python:3.9

ENV PYTHONUNBUFFERED 1


COPY ./dad /dad
COPY /requirements.txt /requirements.txt

WORKDIR /dad
EXPOSE 8000

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home dad



USER dad