import send from './send';
import express from 'express';
import contact from './contact';
import bodyParser from 'body-parser';

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));

app.post('/', contact(send));

app.listen(80, () => console.log('Contact endpoint ready on port 80!'));
