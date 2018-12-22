FROM python:3.7

ENV APP /app

RUN mkdir $APP
WORKDIR $APP

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

#CMD [ "uwsgi", "--ini", "app.ini" ]
CMD ["bash"]