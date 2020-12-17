Warden
======

Deployment
----------

You can build the steward agent image with the following command:
```bash
docker build -t warden:latest .
```

After the image is built you can deploy the agent like this:
```bash
docker run --restart always --env-file .env --name warden -d warden:latest
```
