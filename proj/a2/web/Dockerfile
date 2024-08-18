FROM node:20.16-alpine

LABEL authors="ryan"

WORKDIR /usr/src/

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start" ]
