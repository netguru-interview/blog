# pull official base image
FROM python:3.7-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/app/requirements.txt

# install system dependencies
RUN apk add --virtual .build-deps --no-cache linux-headers build-base postgresql-dev netcat-openbsd jpeg-dev libffi-dev zlib-dev && \
    # install the dependencies required during runtime
    apk add --no-cache libpq jpeg && \
    # https://github.com/pypa/setuptools/issues/2017
    pip install setuptools==45 wheel && \
    # install the actual python packages
    pip install -r requirements.txt && \
    # cleanup the build dependencies
    apk del --purge .build-deps && \
    rm -vrf /var/cache/apk/*

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
