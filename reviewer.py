import requests
from prompts import build_prompt

def review_code(code, language):

    prompt = build_prompt(code, language)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "codellama",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]