from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhookApp", methods = ["POST"])

def webhook():
    output = request.get_json()

    if output and output.get("type") == "url_verification":
        return jsonify ({"challenge": output.get("challenge")})

if __name__ == "__main__":
    app.run()