from flask import Flask, request
from elasticsearch import Elasticsearch

from encoder import Encoder
from utils import create_es_index, create_faiss_index, es_search, faiss_search


# es = Elasticsearch()
# es_indices = create_es_index(es, index="corpus")

encoder = Encoder("small")
faiss_indices = create_faiss_index(encoder)

app = Flask(__name__)


@app.route("/search", methods=["POST"])
def search():
	query = request.json
	# es_result = es_search(es, "corpus", query)
	faiss_result = faiss_search(encoder, faiss_indices, query)
	return result


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8018, threaded=False)
