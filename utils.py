import os
import json

import faiss
import numpy as np


OUTPUT_DIR = "output"


def normalize(sent: str):
	"""Normalize sentence"""
	sent = sent.replace("\n", "")
	return sent


def load_dataset(f_input: str):
	"""Load dataset from input directory"""
	with open(f"{f_input}.json", "r", encoding="utf-8") as corpus:
		lines = [normalize(line["title"]) for line in json.loads(corpus.read())]
		return lines


def es_search(es, index: str, query: str):
	"""Conduct ElasticSearch's search"""
	results = es.search(
		index = index, 
		body = {
			"from":0, 
			"size":10, 
			"query": {
				"match": {
					"query": query,
					"field": "title"
				}
			}
		}
	)
	return results


def create_es_index(es, index: str):
	"""Create ElasticSearch indices"""
	if not es.indices.exists(index=index): 
		es.indices.create(
			index = index,
			body = {
				"settings": {
					"index": {
						"analysis": {
							"analyzer": {
								"my_analyzer": {
									"type": "custom",
									"tokenizer": "nori_tokenizer"
								}
							}
						}
					}
				},
				"mappings": {
					"properties": {
						"id": {
							"type": "long"
						},
						"title": {
							"type": "text",
							"analyzer": "my_analyzer"
						}
					}
				}
			}
		)

		with open(f"{index}.json", encoding="utf-8") as corpus:
			json_data = json.loads(corpus.read())
			body = ""
			for i in json_data:
				body = body + json.dumps({"index": {"_index": "dictionary", "_type": "dictionary_datas"}}) + '\n'
				body = body + json.dumps(i, ensure_ascii=False) + '\n'
			es.bulk(body)


def faiss_search(encoder, indices, query: str, k: int=1):
	"""Conduct FAISS top-k search"""
	query_vec = encoder.encode(query)
	top_k = indices.search(query_vec, k)
	return [
		data[idx] for idx in top_k[1].tolist()[0]
	]



def create_faiss_index(encoder):
	"""Create FAISS indices using encoder"""
	if os.path.exists(f"{OUTPUT_DIR}/faiss.index"):
		indices = faiss.read_index(
	    	os.path.join(OUTPUT_DIR, "faiss.index")
		)
		return indices

	dataset = load_dataset("corpus")
	encoded = [encoder.encode(data) for data in dataset]

	indices = faiss.IndexIDMap(faiss.IndexFlatIP(encoder.dimension))
	indices.add_with_ids(encoded, np.array(range(len(dataset))))

	faiss.write_index(
	    indices,
	    os.path.join(OUTPUT_DIR, "faiss.index")
	)
	return indices
