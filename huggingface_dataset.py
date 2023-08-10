from langchain import ElasticVectorSearch
from langchain.document_loaders import HuggingFaceDatasetLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import huggingface_hub

import os

from langchain.text_splitter import CharacterTextSplitter

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


def split_document():
    dataset_name = "tweet_eval"
    page_content_column = "text"
    name = "stance_climate"

    loader = HuggingFaceDatasetLoader(dataset_name, page_content_column, name)
    #index = VectorstoreIndexCreator().from_loaders([loader])
    #print(index)
    document = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    docs = text_splitter.split_documents(document)
    print(document)
    return docs

# loader.add_elasticsearch_index("context", host="localhost", port="9200", es_index_name="hf_squad_val_context")
