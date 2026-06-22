def generate_digest(results):

    lines = []

    for score, job in results[:10]:

        lines.append(
            f"{job['company']} | {job['title']} | {score:.2f}"
        )

    return "\n".join(lines)