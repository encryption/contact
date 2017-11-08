## Running in Production

1. Add the image to your docker / k8s setup
2. Post form data to the image (http://contact:80)
3. Proxy using nginx to the instance for https support

### Add a service / deployment to your docker compose / kubernetes config.

#### Docker compose

`docker-compose.yml`
```
services:
  web:
    image: zackify/contact:latest
    environment:
    - REDIRECT_URL= #optional. will use request referer if not supplied
    - MAILGUN_KEY=blah
    - MAILGUN_DOMAIN=blah
    - SEND_TO=me@email.com

```

#### Kubernetes

Best practice: Use secrets instead of adding your mailgun info direct to the config file.

`contact-deployment.yml`

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: contact
  creationTimestamp: null
  labels:
    service: contact
spec:
  replicas: 3
  strategy: {}
  template:
    metadata:
      labels:
        service: contact
    spec:
      containers:
      - image: zackify/contact:latest
        name: contact
        env:
        - name: MAILGUN_KEY
          value: "blah"
        - name: MAILGUN_DOMAIN
          value: "blah"
        - name: SEND_TO
          value: "email@gmail.com"
        resources: {}
      restartPolicy: Always
status: {}
```

## Development

- `cp docker-compose.example.yml docker-compose.yml`
- Edit the env variables
- `docker-compose up`


## Testing

Tests will be added soon

`npm test`
