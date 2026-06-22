from app.services.job_scraper import fetch_jobs

jobs = fetch_jobs()

print(
    f"Found {len(jobs)} jobs"
)