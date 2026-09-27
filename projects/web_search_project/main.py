from agents.agent import agent, structured_llm


result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": """
Research El Momento Steakhouse in Islamabad.

Find:
- exact location
- phone number
- description
- what makes it special

Use web search to find this information.
Do not guess or invent information.
"""
        }
    ]
})


raw_response = result["messages"][-1].content

restaurant = structured_llm.invoke(raw_response)

print(restaurant)