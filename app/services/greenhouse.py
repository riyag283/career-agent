import requests


def get_greenhouse_jobs(board_name):

    url = f"https://boards-api.greenhouse.io/v1/boards/{board_name}/jobs"

    response = requests.get(url)

    response.raise_for_status()

    return response.json()