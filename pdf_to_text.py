from langchain.document_loaders import PyMuPDFLoader
loader = PyMuPDFLoader(file_path="https://media.defense.gov/2020/Oct/08/2002514180/-1/-1/0/DOD-DATA-STRATEGY.PDF")
data = loader.load()
print(data[13].page_content)