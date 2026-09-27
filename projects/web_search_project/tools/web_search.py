from dotenv import load_dotenv
from exa_py import Exa
from langchain.tools import tool
import os

load_dotenv()

api_key = os.getenv("EXA_API_KEY")

if not api_key:
    raise ValueError("EXA_API_KEY not found")

exa = Exa(api_key)


@tool
def web_search(query: str) -> str:
    """Search the web for information.

    Args:
        query: The exact search query to send to the web search engine.
    """

    result = exa.search(
        query,
        num_results=5,
        contents={
            "highlights": True
        },
    )

    results = []

    for hit in result.results:
        results.append(
            f"""
Title: {hit.title}
URL: {hit.url}
Highlights: {hit.highlights}
"""
        )

    return "\n".join(results)

# if __name__ == "__main__":
    # result = web_search.invoke(
        # "top restaurants in Islamabad"
    # )

    # print(result)