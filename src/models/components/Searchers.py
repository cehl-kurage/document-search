from abc import ABC, abstractmethod

from langchain.document_loaders import NotionDirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS, Chroma
from subprocess import run


class Searcher(ABC):
    def __init__(
        self,
        chunk_size: int = 10000,
        chunk_overlap: int = 0,
        emb_model="text-embedding-ada-002",
        dir="data/",
    ) -> None:
        self.docs = self.load_docs(dir)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.emb_model = emb_model

    def load_docs(self, dir: str):
        # load documents
        loader = NotionDirectoryLoader(dir)
        docs = loader.load()
        docs = CharacterTextSplitter().split_documents(docs)
        return docs

    @abstractmethod
    def setup(self, api_key):
        pass

    def search(self, query):
        searched_docs = self.model.similarity_search(query, k=1)
        return searched_docs[0].page_content


class FAISSSearcher(Searcher):
    def __init__(
        self,
        chunk_size: int = 10000,
        chunk_overlap: int = 0,
        emb_model="text-embedding-ada-002",
        dir="data/",
    ) -> None:
        super().__init__(chunk_size, chunk_overlap, emb_model, dir)

    def setup(self, api_key):
        self.embedding = OpenAIEmbeddings(model=self.emb_model, openai_api_key=api_key)
        self.model = FAISS.from_documents(self.docs, self.embedding)


class ChromaSearcher(Searcher):
    def __init__(
        self,
        chunk_size: int = 10000,
        chunk_overlap: int = 0,
        emb_model="text-embedding-ada-002",
        dir="data/",
    ) -> None:
        super().__init__(chunk_size, chunk_overlap, emb_model, dir)

    def setup(self, api_key):
        self.embedding = OpenAIEmbeddings(model=self.emb_model, openai_api_key=api_key)
        self.model = Chroma.from_documents(self.docs, self.embedding)

    def search(self, query):
        searched_docs = self.model.similarity_search(query, k=1)
        return searched_docs[0].page_content
