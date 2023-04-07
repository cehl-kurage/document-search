from functools import partial

from langchain.document_loaders import NotionDirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS


class OpenAISearcher:
    def __init__(
        self,
        chunk_size: int = 10000,
        chunk_overlap: int = 0,
        emb_model="text-embedding-ada-002",
        dir="data/",
    ) -> None:
        self.docs = self.load_docs(dir)
        self.emb_model = emb_model

    def load_docs(self, dir: str):
        # load documents
        loader = NotionDirectoryLoader(dir)
        docs = loader.load()
        return docs

    def setup(self, api_key):
        self.embedding = OpenAIEmbeddings(model=self.emb_model, openai_api_key=api_key)
        self.faiss = FAISS.from_documents(self.docs, self.embedding)

    def search(self, query):
        searched_docs = self.faiss.similarity_search(query, k=1)
        return searched_docs[0].page_content
