from langchain.document_loaders import HuggingFaceDatasetLoader
from langchain.llms import huggingface_hub


dataset_name = "tweet_eval"
page_content_column = "text"
name = "stance_climate"


loader = HuggingFaceDatasetLoader(dataset_name, page_content_column, name)
print(loader)