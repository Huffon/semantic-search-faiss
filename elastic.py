from elasticsearch import Elasticsearch

es = Elasticsearch()


def create_es_indices(es):
    """Create ElasticSearch indices"""
    es.indices.create(
        index='dictionary',
        body={
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
                "dictionary_datas": {
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
        }
    )
