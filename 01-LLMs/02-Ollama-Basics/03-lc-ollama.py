from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
llm = Ollama(model="llama2")

llm.invoke("how can langsmith help with testing?")

output_parser = StrOutputParser()
# print(f"reply    length :{len(output_parser)}")
print(f"          type  :{type(output_parser)}")
print(f"          dir   :{dir(output_parser)}")
print(f"          reply :{output_parser}")
print(output_parser)
