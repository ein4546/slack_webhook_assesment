# slack_webhook_assesment
_Webhook setup and JSON Handling Skills Assesment_

**OVERVIEW**

A simple project that **handles Slack's verification URL** sent by Slack during a webhook call/event. Built using **Python (Flask framework)** and deployed using **PythonAnywhere**.

**FEATURES**
* Accepts **POST** as a method.
* Returns value of **"challenge"** for every succesful URL verification.
* Deployed and accesible using **PythonAnywhere**.

**TECH STACK**
* Language: Python
* Framework: Flask
* Host: PythonAnywhere

**HOW IT WORKS**

1. Slack sends a POST request with this payload:\
_{ \
"type": "url_verification",\
"token": "some-token",\
"challenge": "test-challenge-value"\
}_

2. If _"type"="url_verification"_, the webhook extracts the challenge field and returns:\
_{\
  "challenge": "test-challenge-value"\
}_

**DEPLOYMENT STEPS**
1. Uploaded 


