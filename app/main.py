from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

from app.encoder import Encoder
from app.utils import create_es_index, create_faiss_index, es_search, faiss_search


index_name = "corpus"

es = Elasticsearch(["localhost:9200"])
es_indices = create_es_index(es, index=index_name)

encoder = Encoder("small", dimension=256)
faiss_indices = create_faiss_index(encoder)

app = Flask(__name__)


@app.route("/search", methods=["POST"])
def search():
    query = request.json["query"]
    es_result = es_search(es, index_name, query)
    faiss_result = faiss_search(encoder, faiss_indices, query)
    result = {
        "elastic": es_result,
        "faiss": faiss_result,
    }
    return jsonify(result)


@app.route("/")
def index():
    return "Hello, Semantic Search!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8018, threaded=False)
