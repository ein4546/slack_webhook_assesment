# slack_webhook_assesment
_Webhook setup and JSON Handling Skills Assesment_

**Live Webhook URL:** http://ein4546.pythonanywhere.com/webhookApp

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
1. Slack sends a POST request, including a JSON field name/key "type" and "challenge" and their respective values.
2. If JSON field name/key contains value "url_verification", the webhook would return the field "challenge" as a response.

**DEPLOYMENT STEPS**
1. Commit code in Github.
2. Create account in _https://www.pythonanywhere.com/_
3. Under _Web_, add new Web App.
4. Under _Consoles_, add virtual environment to host app.
5. Clone the git repository in the virtual environment using _git clone_.
6. Install necessary requirements in the virtual environment, to be able to run the .py file.
7. Configure Web setup.

**HOW TO TEST THE WEBHOOK**

Using _POSTMAN_, send a POST request with the payload:

![image](https://github.com/user-attachments/assets/81ee6c83-f8c7-44b6-b54f-df1ab38ad93f)


Expected Response:

![image](https://github.com/user-attachments/assets/3772912a-3532-4d94-a741-76c9f4d188f0)







