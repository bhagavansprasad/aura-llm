from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_core.documents import Document

llm = Ollama(model="llama2")

print("1")
# llm.invoke("how can langsmith help with testing?")

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "how can langsmith help with testing?"})
print(response["answer"])
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])


print("2")

chain = prompt | llm 
chain.invoke({"input": "how can langsmith help with testing?"})

print("3")

output_parser = StrOutputParser()
# print(f"reply    length :{len(output_parser)}")
print(f"          type  :{type(output_parser)}")
print(f"          reply :{output_parser}")
print(output_parser)

print("4")

chain = prompt | llm | output_parser
chain.invoke({"input": "how can langsmith help with testing?"})

print("5")
