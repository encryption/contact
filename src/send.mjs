import mailgun from 'mailgun-js';

let email = mailgun({
  apiKey: process.env.MAILGUN_KEY,
  domain: process.env.MAILGUN_DOMAIN,
});

export default data =>
  new Promise((resolve, reject) => {
    var message = {
      from: 'Encryption, Inc <hello@encryption.io>',
      to: process.env.SEND_TO,
      subject: 'New Contact Form Submission!',
      text: Object.keys(data)
        .map(key => `${key}: ${data[key]}`)
        .join('\n'),
    };

    email.messages().send(message, function(error, body) {
      if (error) return reject(error);
      resolve(body);
    });
  });
