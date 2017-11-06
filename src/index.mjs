import express from 'express';
import bodyParser from 'body-parser';

const app = express();

app.use(bodyParser());

app.post('/', function(request, response) {
  console.log(request.body.user.name);
  console.log(request.body.user.email);
});

app.listen(80, () => console.log('Contact endpoint ready on port 80!'));
