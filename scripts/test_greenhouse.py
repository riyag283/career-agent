from app.services.greenhouse import get_greenhouse_jobs

jobs = get_greenhouse_jobs("databricks")

for job in jobs["jobs"][:10]:
    print(job["title"])