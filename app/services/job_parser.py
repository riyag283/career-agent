def parse_greenhouse_job(job):

    return {
        "id": job["id"],
        "title": job["title"],
        "location": job["location"]["name"],
        "url": job["absolute_url"]
    }