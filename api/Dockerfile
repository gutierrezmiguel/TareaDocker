FROM alpine:3.10

RUN apk add --no-cache python3-dev \ 
    && pip3 install --upgrade pip

WORKDIR /api

COPY . /api

RUN pip3 --no-cache-dir install -r requirements.txt

ENTRYPOINT ["python3" , "app.py"]

