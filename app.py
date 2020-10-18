from flask import Flask
from flask import jsonify
from dotenv import load_dotenv

from src.domain import environments

load_dotenv(".env")

app = Flask(__name__)


@app.route('/health-check', methods=['GET'])
def health_check():
    return jsonify({"message": "Process running!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=environments.PORT, debug=environments.DEV_MODE)
