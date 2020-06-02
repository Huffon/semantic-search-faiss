from flask import Flask, request
from encoder import Encoder


encoder = Encoder()
app = Flask(__name__)


@app.route("/search", methods=["POST"])
def search():
	data = request.json


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8018, threaded=False)
