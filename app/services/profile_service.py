import json
from pathlib import Path


def load_profile():

    with open("data/profile.json", "r") as f:
        return json.load(f)


def get_keywords():

    profile = load_profile()

    keywords = []

    keywords.extend(profile["target_roles"])

    keywords.extend(profile["skills"])

    return [
        keyword.lower()
        for keyword in profile["search_keywords"]
    ]