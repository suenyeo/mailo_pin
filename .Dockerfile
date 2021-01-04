FROM python:3.9.0

WORKDIR /home/

RUN echo "make_imgaes.."

RUN git clone https://github.com/suenyeo/mailo_pin.git

WORKDIR /home/mailo_pin/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=i)1di1blw0v*n2-bo&aist867x%ay*w)ru)r=&z5(ly-p2)l@4" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=mailo_pin.settings.deploy && python manage.py collectstatic --settings=mailo_pin.settings.deploy &&  gunicorn mailo_pin.wsgi --env DJANGO_SETTINGS_MODULE=mailo_pin.settings.deploy --bind 0.0.0.0:8000"]