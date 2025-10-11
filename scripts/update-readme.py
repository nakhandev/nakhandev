"""
🧩 update-readme.py
Automatically updates the main README.md with live GitHub stats and project info.
"""

import requests
from datetime import datetime

USERNAME = "nakhandev"
README_PATH = "README.md"

def fetch_github_stats(username):
    url = f"https://api.github.com/users/{username}"
    data = requests.get(url).json()
    return {
        "public_repos": data.get("public_repos", 0),
        "followers": data.get("followers", 0)
    }

def update_readme():
    stats = fetch_github_stats(USERNAME)
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content.replace(
        "<!--stats-->",
        f"Public Repos: **{stats['public_repos']}** | Followers: **{stats['followers']}** (Last updated: {datetime.now():%Y-%m-%d})"
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
