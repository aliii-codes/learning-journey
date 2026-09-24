import os
from dotenv import load_dotenv
from langchain.tools import tool
from github import Github, Auth

load_dotenv()
os.environ["GITHUB_TOKEN"] = os.getenv("GITHUB_TOKEN")



def get_github_clients() -> Github:
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise ValueError("GITHUB_TOKEN is not set in the environment variables.")

    return Github(auth=Auth.Token(token))

@tool
def get_github_repo(repo_name: str) -> str:
    """Get basic information about a GitHub repository."""

    github = get_github_clients()
    repo = github.get_repo(repo_name)

    return (
        f"Repository: {repo.full_name}\n"
        f"Description: {repo.description}\n"
        f"Stars: {repo.stargazers_count}\n"
        f"Forks: {repo.forks_count}\n"
        f"Language: {repo.language}\n"
        f"URL: {repo.html_url}"
    )