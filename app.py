from flask import Flask, jsonify, request
from dotenv import load_dotenv

from src.domain import environments
from src.applications import BoostrapApplication

load_dotenv(".env")

app = Flask(__name__)


@app.before_first_request
def setup_webhooks():
    BoostrapApplication.BootstrapApplication()


@app.route('/health-check', methods=['GET'])
def health_check():
    return jsonify({"message": "Process running!"})


@app.route('/webhook/<path:path>', methods=['POST'])
def chat_webhook(path):
    print(request.json)
    return jsonify({"message": "Process running!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=environments.PORT, debug=environments.DEV_MODE)
