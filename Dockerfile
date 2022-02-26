FROM node:17.6.0-buster-slim

RUN npm install hexo-cli -g

RUN mkdir -p /blog/
RUN hexo init blog

VOLUME /blog/
WORKDIR /blog/

RUN npm install

EXPOSE 4000

ENTRYPOINT ["hexo"]
