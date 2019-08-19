FROM alpine


RUN apk update && \
    mkdir /app
COPY . /app
WORKDIR /app
RUN apk --no-cache add python3 python3-dev git &&\
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt && \
    pip3 install gunicorn

EXPOSE 5000