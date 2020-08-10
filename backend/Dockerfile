FROM python:3.7-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt

# install system dependencies
RUN apk add --virtual .build-deps --no-cache linux-headers build-base postgresql-dev netcat-openbsd jpeg-dev libffi-dev zlib-dev && \
    # install the dependencies required during runtime
    apk add --no-cache libpq jpeg && \
    # https://github.com/pypa/setuptools/issues/2017
    pip install setuptools==45 wheel && \
    # install the actual python packages
    pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt && \
    # cleanup the build dependencies
    apk del --purge .build-deps && \
    rm -vrf /var/cache/apk/*

RUN pip install flake8
# copy project
COPY . /usr/src/app/
RUN flake8 --ignore=E501,F401 .

FROM python:3.7-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN apk add --no-cache libpq jpeg
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

EXPOSE 8080

CMD ["/usr/local/bin/uwsgi", "--ini", "uwsgi.ini"]
