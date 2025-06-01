import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Clarity Coach", page_icon="🧠")

st.title("🧠 Clarity Coach")
st.markdown("Refine your writing. Get feedback. Become clear.")

user_input = st.text_area("✍️ Paste your message here", height=200)

if "history" not in st.session_state:
    st.session_state.history = []
    
if st.button("🔍 Analyze"):
    if not user_input.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Analyzing..."):
            prompt = f"""
You are a Clarity Coach. A user has written the following text:

\"\"\"{user_input}\"\"\"

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
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=500
            )

            result = response.choices[0].message.content
            st.markdown("### 🧠 Coaching Output")
            st.code(result, language='markdown')
            
            st.button("📋 Copy Improved Version", on_click=lambda: st.session_state.update({"copied_text": result}))

            # Save to history
            st.session_state.history.append({
                "input": user_input,
                "output": result
            })

if st.session_state.history:
    st.markdown("### 🕘 Previous Messages")
    for i, item in enumerate(reversed(st.session_state.history), 1):
        st.markdown(f"**{i}. Original**: {item['input']}")
        st.markdown(f"**Improved:**\n{item['output']}")
        st.markdown("---")
