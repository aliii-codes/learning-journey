import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from tools import get_github_repo
from schemas import RepoReport



load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    max_tokens=2048,
    temperature=0.7
)


agent = create_agent(
    model=llm,
    tools=[get_github_repo],
    # response_format=RepoReport
)

result = agent.invoke({
    "messages" : [
        {
            "role" : "user",
            "content" : "compare aliii-codes/Orbit with aliii-codes/learning-journey"
        }
    ]
})

# print(result["structured_response"])
print(result["messages"][-1].content)