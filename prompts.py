def build_prompt(code, language):

    prompt = f"""
You are a senior software engineer performing a strict code review.

Review the following {language} code and identify:

1. Syntax errors
2. Logical bugs
3. Code quality issues
4. Best practice improvements
5. Provide corrected code

Return your response in this format:

Syntax Errors:
- ...

Logical Bugs:
- ...

Improvements:
- ...

Corrected Code:
...

Code to review:
{code}
"""

    return prompt