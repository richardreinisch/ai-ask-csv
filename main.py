
from langchain.chains import create_retrieval_chain
from langchain.chains import RetrievalQA
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_ollama import OllamaLLM
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate


llm = OllamaLLM(model="llama3.2", temperature=0)

embed_model = OllamaEmbeddings(model="llama3.2")

loader = CSVLoader(file_path="./data/test.csv", csv_args={"delimiter": ";", "fieldnames": ["id", "company", "short", "text", "meta"]})
documents = loader.load()

vector_store = Chroma(embedding_function=embed_model)
vector_store.add_documents(documents)

retriever = vector_store.as_retriever()

chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="refine", # "map_reduce", "refine" oder "stuff"
    return_source_documents=True,
    verbose=True
)

system_template = """
Answer any use questions based solely on the context below:

<context>
{context}
</context>
"""

human_template = """{input}"""

retrieval_qa_chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template)
])

combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)

retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

response = retrieval_chain.invoke({"input": "Please find a company related to sports equipment for athletes, add all details?"})
# response = retrieval_chain.invoke({"input": "Please find a company related to online learning, add all details?"})
# response = retrieval_chain.invoke({"input": "Please find a company related to pets, add all details?"})

print(response["answer"])
