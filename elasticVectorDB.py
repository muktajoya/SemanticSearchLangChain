import os

## for vector store
from langchain.vectorstores import ElasticVectorSearch


def setup_vectordb(hf, doc):
    # Elasticsearch URL setup
    print(">> Prep. Elasticsearch config setup")
    print(hf)
    # endpoint = os.getenv('ES_SERVER', 'ERROR')
    # username = os.getenv('ES_USERNAME', 'ERROR'), # elastic
    # password = os.getenv('ES_PASSWORD', 'ERROR')  # uF2VwqvCqrTSQvD2dvoUyeRS

    elastic_host =  "cluster_id.us-central1.gcp.cloud.es.io"

    index_name = "test_index"

    elasticsearch_url = f"https://username:password@{elastic_host}:9200"


    #return ElasticVectorSearch.from_documents(doc, embedding=hf, elasticsearch_url=url)
    return ElasticVectorSearch(embedding=hf, elasticsearch_url=elasticsearch_url, index_name=index_name), elasticsearch_url