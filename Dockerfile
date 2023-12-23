###########
# BUILDER #
###########

# pull official base image
FROM python:3.11.3-slim-buster as builder
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# lint
RUN pip install --upgrade pip
RUN pip install flake8==6.0.0
COPY . /usr/src/app/
# RUN flake8  --ignore=E501,F401 ./wiserly_app/services

# install python dependencies
COPY ./wiserly_app/requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.11.3-slim-buster

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*



# copy entrypoint-prod.sh
COPY ./wiserly_app/entrypoint.prod.sh $APP_HOME

# copy project
COPY . $APP_HOME

#copy templates
COPY  --from=builder /usr/src/app/wiserly_app/services/shopify_bp/templates/*.html $APP_HOME/templates/static/
COPY --from=builder /usr/src/app/wiserly_app/services/shopify_bp/templates/static/ $APP_HOME/templates/static/

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app
EXPOSE 5000
# run entrypoint.prod.sh

ENV SHOPIFY_API_KEY="c5490bfc44800dc22a6c7e67385c93ef"
ENV SHOPIFY_SHARED_SECRET="3b4c279c656b60557df965d0851cd368"
ENV HOSTNAME_FOR_SHOPIFY="https://88da-2409-4062-220c-5bfd-b4a9-b1e3-a414-1bdf.ngrok-free.app"
ENV SHOPIFY_API_VERSION=2023-01
ENV SHOPIFY_BILLING_TEST_MODE="true"
ENV WEBHOOK_TEST_MODE="false"
ENV DATABASE_URL=postgresql+psycopg2://wiserly_02:prodpassword@postgresql-155691-0.cloudclusters.net:18598/wiserlydb_02
ENV ENVFLASK_DEBUG=0
ENV POSTGRES_DB="wiserlydb_02"
ENV POSTGRES_USER="wiserly_02"
ENV POSTGRES_PASSWORD="prodpassword"
ENV APP_FOLDER="/home/app/web"
ENV SQL_HOST="postgresql-155691-0.cloudclusters.net"
ENV SQL_PORT=18598
ENV DATABASE="wiserlydb_02"
ENV FLASK_ENV="prod"
ENTRYPOINT ["gunicorn"]
CMD ["manage:app"]
# ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]