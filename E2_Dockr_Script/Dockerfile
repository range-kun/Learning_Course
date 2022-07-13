FROM alpine:latest
RUN  mkdir /home/favicon
WORKDIR /home
COPY ./script ./script
ENV SOURCE="yandex.ru"
CMD ["sh", "-c", "/home/script/script.sh ${SOURCE}"]
