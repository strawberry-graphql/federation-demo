FROM node:16

WORKDIR /app

COPY package* /app/
RUN npm ci
COPY . /app/

CMD node index.js
