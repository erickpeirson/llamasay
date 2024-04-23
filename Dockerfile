FROM alpine
RUN apk add --no-cache perl
COPY llamasay /usr/local/bin/llamasay
COPY chaos.llama /usr/local/share/llamas/default.llama
ENTRYPOINT ["/usr/local/bin/llamasay"]
