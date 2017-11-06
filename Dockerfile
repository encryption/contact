FROM node:9.0.0

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install

COPY . .

CMD ./node_modules/.bin/nodemon --watch "./src" -x "node --experimental-modules" src/index.mjs
EXPOSE 8888