FROM alpine

RUN apk add --no-cache perl python3

ENV PYTHONUNBUFFERED=1
COPY llamasay /usr/local/bin/llamasay
COPY llamaserv.py /usr/local/bin/llamaserv.py
COPY chaos.llama /usr/local/share/llamas/default.llama
ENTRYPOINT ["/usr/local/bin/llamasay"]
