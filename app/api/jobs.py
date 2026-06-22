from fastapi import APIRouter
from app.services.job_scraper import fetch_jobs

router = APIRouter()


@router.get("/jobs")
def get_jobs():
    return fetch_jobs()