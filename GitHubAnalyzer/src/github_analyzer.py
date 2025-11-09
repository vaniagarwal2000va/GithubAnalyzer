import os
import requests

import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
if not TOKEN:
    print('No token')
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response  =  requests.get(url, headers = HEADERS)
    if response.status_code == 200:
        data = response.json()
        repos =  [repo["name"] for repo in data]
        return repos
    else:
        return []
    
def get_commit_activity(username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        commits = response.json()
        return len(commits)
    else:
        return 0

def visualize_datframe(dataframe):
    dataframe =  dataframe.sort_values(by="Commits", ascending =False)
    plt.figure(figsize=(10,5))
    plt.bar(dataframe["Repository"], dataframe["Commits"], color="skyblue")
    plt.title(f"Github Commit A ctivity for {user}")
    plt.xlabel("Repositories")
    plt.ylabel("Number of Commits")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    user  =  input ("Enter github usernmame").strip()
    repos =  get_repos(user)
    data = []
    for repo in repos:
        commits = get_commit_activity(user, repo)
        data.append({"Repository": repo, "Commits":commits})

    df = pd.DataFrame(data)
    visualize_datframe(dataframe=df)






