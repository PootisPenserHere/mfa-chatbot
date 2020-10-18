from flask import Flask
from flask import jsonify
from dotenv import load_dotenv

import os

load_dotenv(".env")

app = Flask(__name__)


@app.route('/health-check', methods=['GET'])
def health_check():
    return jsonify({"message": "Process running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("APP_PORT")), debug=bool(os.getenv("DEV_MODE") == "true"))
