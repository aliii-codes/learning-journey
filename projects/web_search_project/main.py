import os

from agent import agent
from llm import llm
from schema import RestaurantInfo, RestaurantList



result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Find 5 good restaurants in Islamabad. Use web search. 2026"
        }
    ]
})

raw_response = result["messages"][-1].content



names_response = llm.invoke(
    f"""
Extract all restaurant names from the research below.

Return ONLY the restaurant names, one per line.
No numbering.
No explanations.

Research:
{raw_response}
"""
)

restaurant_names = names_response.content.strip().splitlines()



structured_llm = llm.with_structured_output(RestaurantInfo)

restaurants = []

for name in restaurant_names:

    restaurant = structured_llm.invoke(
        f"""
Extract information about {name} from the research below.

Return a RestaurantInfo object.

If information is unavailable, use null.

Research:
{raw_response}
"""
    )

    restaurants.append(restaurant)



restaurant_list = RestaurantList(
    restaurants=restaurants
)



output_path = os.path.join(
    os.path.dirname(__file__),
    "output.json"
)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(restaurant_list.model_dump_json(indent=4))