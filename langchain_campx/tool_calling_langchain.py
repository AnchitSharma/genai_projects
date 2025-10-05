
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

# tool create 
@tool
def multiply(a: int, b:int) -> int:
    """Given 2 numbers a and b this tool return their product"""
    return a * b

print(multiply.invoke({'a':3, 'b':4}))
multiply.name
multiply.args
multiply.description


MODEL = "qwen3"
llm = ChatOllama(
    model = MODEL
)

llm_with_tools = llm.bind_tools([multiply])

# print("--- Invoking with a non-tool-related prompt ---")
# print(llm_with_tools.invoke("Hi How are you ?"))


print(llm_with_tools.invoke("can you multiply 3 with 10"))

