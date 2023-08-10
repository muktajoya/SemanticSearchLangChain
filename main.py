# This is a sample Python script.
from langchain import ElasticVectorSearch, FAISS

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import huggingface_dataset
import embedding
import elasticVectorDB
import llm_chain

embedding = embedding.setup_embeddings()
doc_chunks = huggingface_dataset.split_document()
db, url = elasticVectorDB.setup_vectordb(embedding,doc_chunks)  ## Elasticsearch as a vector db
llm_chain_informed = llm_chain.make_the_llm()  ## set up the conversational LLM

elastic_db= db.from_documents(doc_chunks,embedding, elasticsearch_url=url)

#elsticsearch_db = db.from_documents(doc_chunks, embedding, elasticsearch_url=url)  ##Create the vectorized db

## how to ask a question
def ask_a_question(question):

    ## 3. get the relevant chunk from Elasticsearch for a question
    similar_docs = elastic_db.similarity_search(question)
    print(f'The most relevant passage: \n\t{similar_docs[0].page_content}')

    ## 4. Ask Local LLM context informed prompt
    informed_context= similar_docs[0].page_content
    response = llm_chain_informed.run(context=informed_context,question=question)
    return response



while True:
    command = input("User Question>> ")
    response = ask_a_question(command)
    print(f"\n\n I think the answer is : {response}\n")



