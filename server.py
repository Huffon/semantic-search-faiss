from flask import Flask, request
from encoder import Encoder
from utils import create_index, search


encoder = Encoder("small")
indices = create_index(encoder)

app = Flask(__name__)


@app.route("/search", methods=["POST"])
def search():
	query = request.json
	result = search(encoder, indices, query)
	return result


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8018, threaded=False)
