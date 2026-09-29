from langchain.agents import create_agent

from tools import web_search
from llm import llm





agent = create_agent(
    model=llm,
    tools=[web_search],
)