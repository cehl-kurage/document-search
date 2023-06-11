from dotenv import load_dotenv
from langchain.document_loaders import NotionDirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

load_dotenv()

loader = NotionDirectoryLoader("data/")
documents = loader.load()
# text_splitter = CharacterTextSplnitter(chunk_size=1000, chunk_overlap=0)
# docs = text_splitter.split_documents(documents)
docs = documents

embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(docs, embeddings)

query = "円を綺麗に描画する方法教えてください"
docs = db.similarity_search(query)

print(docs[0].page_content)
