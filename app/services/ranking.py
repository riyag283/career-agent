from sklearn.metrics.pairwise import cosine_similarity

def rank_jobs(profile_vector, jobs):

    results = []

    for job in jobs:

        score = cosine_similarity(
            [profile_vector],
            [job["embedding"]]
        )[0][0]

        results.append(
            (score, job)
        )

    return sorted(
        results,
        reverse=True
    )