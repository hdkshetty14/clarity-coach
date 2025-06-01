import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)

def clarity_check(text):
    prompt = f"""
You are a Clarity Coach. A user has written the following text:

\"\"\"{text}\"\"\"

Your task:

Step 1: Rate the following from 1 to 10:
- Clarity
- Structure
- Brevity

Step 2: Give 3 specific suggestions for improvement (no fluff).

Step 3: Rewrite the message to make it clearer, more concise, and more structured.

Format your reply like this:
---
Clarity: x/10  
Structure: x/10  
Brevity: x/10  

Feedback:
• ...
• ...
• ...

Improved Version:
"..."
---
    """

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=500
    )

    return response.choices[0].message.content

# === MAIN SCRIPT ===
if __name__ == "__main__":
    print("🔍 Clarity Coach — Paste your text below:\n")
    user_input = input(">> ")
    print("\n🧠 Coaching Output:\n")
    result = clarity_check(user_input)
    print(result)
