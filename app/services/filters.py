from app.services.profile_service import get_keywords

EXCLUDED_KEYWORDS = [
    "sales",
    "marketing",
    "finance",
    "legal",
    "hr",
]


def is_relevant_job(title):

    title = title.lower()

    if any(
        word in title
        for word in EXCLUDED_KEYWORDS
    ):
        return False

    keywords = get_keywords()

    return any(
        keyword in title
        for keyword in keywords
    )