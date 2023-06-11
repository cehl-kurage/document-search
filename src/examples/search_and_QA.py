from dotenv import load_dotenv
from langchain.document_loaders import NotionDirectoryLoader
from langchain.document_loaders import WikipediaLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

load_dotenv()

# loader = NotionDirectoryLoader("data/")
# documents = loader.load()

print("loading documents from wikipedia(remote)")
documents = WikipediaLoader(query="東京理科大学", load_max_docs=50, lang="ja").load()
print("finish loading")

# text_splitter = CharacterTextSplnitter(chunk_size=1000, chunk_overlap=0)
# docs = text_splitter.split_documents(documents)
docs = documents

embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(docs, embeddings)

query = "lorenz曲線の描き方を教えてください。"
docs = db.similarity_search(query)

information = docs[0].page_content
from langchain import LLMChain, OpenAI, PromptTemplate

template = """
# 質問
{question}
# 該当ページ
```
{information}
```
# 回答
"""
prompt = PromptTemplate(template=template, input_variables=["question", "information"])
llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

answer = llm_chain.predict(question=query, information=information)
print(answer)
