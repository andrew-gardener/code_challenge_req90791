# syntax=docker/dockerfile:1
FROM node:18.9
ENV NODE_ENV=dev
WORKDIR /app

# install deps
COPY package.json .
RUN yarn

# copy source
COPY . .

EXPOSE 80

CMD yarn dev