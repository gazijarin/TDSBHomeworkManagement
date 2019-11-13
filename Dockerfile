# Followed tutorial from: https://testdriven.io/blog/deploying-flask-to-heroku-with-docker-and-gitlab/ and lecture tutorial 3.2
# for this Dockerfile. Mainly following the way they used Nginx in order to serve the Vue front end while also
# forwarding the API from the Flask back-end.

FROM nginx:stable-alpine
RUN apk update && apk add python3 \
    py-pip \
    python3-dev \
    gcc \
    bash \
    nodejs npm

WORKDIR /tdsb
COPY ./front-end front-end/
RUN cd front-end && npm install
RUN cd front-end && npm run build
RUN /bin/bash -c "cp -r front-end/dist/. /usr/share/nginx/html"

COPY ./server/default.conf.template /etc/nginx/conf.d/default.conf.template
COPY ./server server/
RUN pip install -r server/requirements.txt gunicorn
CMD gunicorn -b 0.0.0.0:5000 wsgi:app --chdir "/tdsb/server" --daemon && \
      /bin/bash -c "envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf" && \
      nginx -g 'daemon off;'