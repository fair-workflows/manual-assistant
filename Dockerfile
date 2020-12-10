FROM continuumio/miniconda3:4.9.2

RUN mkdir /app

COPY ./ /app/

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT python app.py

EXPOSE 8080