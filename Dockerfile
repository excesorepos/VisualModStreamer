FROM python:3.7-alpine
RUN mkdir /app
RUN apk add make automake gcc g++ subversion python3-dev gcc libxslt-dev
ADD requirements.txt /app
ADD visualmod_streamer.py /app
RUN addgroup -S visualmod && adduser -S visualmod -G visualmod
RUN chown -R visualmod: /app
USER visualmod
WORKDIR /app
RUN pip3 install -r /app/requirements.txt
CMD ["python", "/app/visualmod_streamer.py"]