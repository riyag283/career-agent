import requests

def fetch_jobs():

    jobs = []

    companies = [
        "Google",
        "Uber",
        "Databricks"
    ]

    for company in companies:

        jobs.append({
            "company": company,
            "title": "Software Engineer"
        })

    return jobs