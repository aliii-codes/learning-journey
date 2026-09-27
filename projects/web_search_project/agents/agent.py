from langchain.agents import create_agent

from llm.llm import llm
from tools.web_search import web_search
from schemas.schema import Restaurant, RestaurantList

agent = create_agent(
    model=llm,
    tools=[web_search],
    # response_format=RestaurantList,
)

structured_llm = llm.with_structured_output(RestaurantList)