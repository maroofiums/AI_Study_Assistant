from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = MistralAIEmbeddings()