# TARGET_COMPANIES = [
#     "Google",
#     "Meta",
#     "Databricks",
#     "Snowflake",
#     "Stripe",
#     "Uber",
#     "Cloudflare",
#     "Confluent",
#     "MongoDB",
#     "Anthropic",
#     "OpenAI"
# ]


# def fetch_jobs():
#     jobs = []

#     for company in TARGET_COMPANIES:
#         jobs.append({
#             "company": company,
#             "title": "Placeholder Job",
#             "location": "Unknown"
#         })

#     return jobs

from app.services.greenhouse import get_greenhouse_jobs
from app.services.job_parser import parse_greenhouse_job

def fetch_jobs():

    jobs = get_greenhouse_jobs("databricks")

    return [
        parse_greenhouse_job(job)
        for job in jobs["jobs"]
    ]