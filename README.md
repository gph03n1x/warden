Warden
======

Warden is a simple periodic service which notifies a discord 
channel through a webhook when your IP address changes. This can be quite useful when you have Machines that are not assigned a static IP address but, they include a bunch of services which can be accessed through the web.


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
