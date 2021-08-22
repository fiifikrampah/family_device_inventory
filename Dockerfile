FROM python:3.9.6-slim-buster

RUN mkdir /code
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app/views.py" ]
