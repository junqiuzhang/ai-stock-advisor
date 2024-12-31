import os
import getpass

from langchain_openai import AzureChatOpenAI
from langchain_core.globals import set_llm_cache
from langchain_core.caches import InMemoryCache
from langchain_core.runnables import chain
from langchain_core.tools import tool
from langchain_core.output_parsers import PydanticToolsParser, StrOutputParser


@tool
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b."""
    return a * b


tools_list = [add, multiply]
tools_dict = {
    "add": add,
    "multiply": multiply,
}


@chain
def use_tool(msg):
    if not hasattr(msg, "tool_calls"):
        raise ValueError("Message must have a 'tool_calls' attribute.")
    if len(msg.tool_calls) == 0:
        raise ValueError("Message must have at least one tool call.")
    if len(msg.tool_calls) > 1:
        raise ValueError("Message must have only one tool call.")
    tool_call = msg.tool_calls[0]
    selected_tool = tools_dict[tool_call["name"]]
    tool_msg = selected_tool.invoke(tool_call)
    return tool_msg


if __name__ == "__main__":
    if not os.environ.get("AZURE_OPENAI_API_KEY"):
        os.environ["AZURE_OPENAI_API_KEY"] = getpass.getpass("Enter API key for Azure: ")

    set_llm_cache(InMemoryCache())

    llm = AzureChatOpenAI(
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
        openai_api_version=os.environ["AZURE_OPENAI_CHAT_API_VERSION"],
    )

    llm_with_tools = llm.bind_tools(tools_list)

    my_chain = llm_with_tools | use_tool | StrOutputParser()

    print(my_chain.invoke("What is 3 * 12?"))
