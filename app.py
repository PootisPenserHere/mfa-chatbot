from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/health-check', methods=['GET'])
def health_check():
    return jsonify({"message": "Process running"})


if __name__ == "__main__":
    app.run()
