import os

from dotenv import load_dotenv
from langchain.document_loaders import NotionDirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI-API-KEY")

loader = NotionDirectoryLoader("data/")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

db = FAISS.from_documents(docs, embeddings)

query = "rolenz曲線を描く方法を教えてください。"
docs = db.similarity_search(query)

print(docs[0].page_content[:30])
