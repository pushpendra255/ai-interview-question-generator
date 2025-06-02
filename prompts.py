
from groq import Groq

# Replace with your actual Groq API key
client = Groq(api_key="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")

def generate_questions(tech_list):
    all_questions = {}
    for tech in tech_list:
        prompt = (
            f"You are a technical recruiter. Generate 3-5 technical questions for a candidate proficient in {tech}."
        )
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful recruiter assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        questions_text = response.choices[0].message.content
        all_questions[tech] = [q.strip("- ") for q in questions_text.strip().split("\n") if q.strip()]
    return all_questions
