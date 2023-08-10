# SemanticSearchLangChain
1. Here use Huggingface dataset (https://huggingface.co/datasets/tweet_eval)
2. Dataset is divided into small chunks
3. Each chunk of text is handed to a sentence transformer, which generates a dense vector to represent its semantic meaning as a vector embedding.Here i use Hugging face embedding (sentence-transformers/all-mpnet-base-v2)
4. The chunks are stored in Elasticsearch with their vector embeddings
5. When a question is asked, a vector is created for the question and then Elasticsearch is queried to find the  semantically closest chunk to the question.
6. A prompt template is composed for a LLM that  the retrieved text chunk in as extra contextual knowledge. I use HuggingfacePipeline to run the model. (model_id = 'google/flan-t5-large')
7. The LLM serve a relevant answer to the question.
# As VectorDatabase, ElasticVectorSearch is used. Two efficient way to use ElasticVector 
# -locally with Docker
# -with Elastic Cloud URL (you have to create a cluster id, host ,username and password).
