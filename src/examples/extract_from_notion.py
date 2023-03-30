from langchain.document_loaders import NotionDirectoryLoader

loader = NotionDirectoryLoader("data/VRC")
docs = loader.load()

for i in docs:
    print(i.summary)
