import os
import faiss


OUTPUT_DIR = "output"


def search(encoder, indices, query: str, k: int=1):
	"""Conduct top-k search"""
	query_vec = encoder.encode(query)
	top_k = indices.search(query_vec, k)
	return [
		data[idx] for idx in top_k[1].tolist()[0]
	]


def load_dataset(input_dir: str):
	"""Load dataset from input directory"""
	with open(input_dir, "r", encoding="utf-8") as corpus:
		lines = corpus.readlines()
		return lines


def create_index(encoder):
	"""Create FAISS indices using encoder"""
	if os.path.exists(f"{OUTPUT_DIR}/faiss.index"):
		indices = faiss.read_index(
	    	os.path.join(OUTPUT_DIR, "faiss.index")
		)
		return indices

	dataset = load_dataset()
	encoded = [encoder.encode(data) for data in dataset]

	indices = faiss.IndexIDMap(faiss.IndexFlatIP(encoder.dimension))
	indices.add_with_ids(encoded, np.array(range(len(dataset))))

	faiss.write_index(
	    indices,
	    os.path.join(OUTPUT_DIR, "faiss.index")
	)
	return indices
