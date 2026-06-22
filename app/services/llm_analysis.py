from openai import OpenAI

client = OpenAI()

def analyze(job, profile):

    prompt = f"""
    Profile:
    {profile}

    Job:
    {job}

    Explain:
    - Why match
    - Missing skills
    - Interview prep areas
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text