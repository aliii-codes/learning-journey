import os

from dotenv import load_dotenv
from exa_py import Exa
from langchain.tools import tool

load_dotenv()

exa = Exa(api_key=os.getenv("EXA_API_KEY"))


@tool
def web_search(query: str) -> str:
    """Search the web for information about restaurants."""

    results = exa.search(
        query,
        num_results=5,
        contents={
            "highlights": True
        }
    )

    output = []

    for result in results.results:
        output.append(
            f"""
Title: {result.title}
URL: {result.url}
Highlights: {result.highlights}
"""
        )

    return "\n".join(output)