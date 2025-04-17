# dax_to_sql_openrouter.py

import streamlit as st
import requests
import os

# Set your OpenRouter API key
API_KEY = st.secrets["OPENROUTER_API_KEY"] if "OPENROUTER_API_KEY" in st.secrets else os.getenv("OPENROUTER_API_KEY")

# OpenRouter endpoint for text generation
OPENROUTER_API_URL = "https://api.openrouter.ai/v1/engines/mistral-7b-instruct-v0.2/completions"

st.title("🧠 DAX to SQL Translator + Explainer using OpenRouter")

st.markdown("""
Paste any DAX expression below and get:
- A plain English explanation
- An SQL translation (if possible)
- Any context-related warnings
""")

# DAX Input
dax_input = st.text_area("🔤 Enter your DAX formula here", height=200)

if st.button("🧠 Translate & Explain") and dax_input.strip():
    with st.spinner("Thinking..."):
        prompt = f"""
You are an expert in DAX and SQL.

Given the following DAX formula:

{dax_input}

Please:
1. Explain in plain English what this DAX measure or expression is doing.
2. Translate it to a SQL equivalent query, assuming relational database structure.
3. Point out any limitations where SQL can't fully mimic DAX behavior, especially due to evaluation or filter context.

Be concise and helpful.
"""

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "prompt": prompt,
            "max_tokens": 500,
            "temperature": 0.2
        }

        # Send the request to OpenRouter API
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()['choices'][0]['text']
            st.markdown("### 💬 Result")
            st.markdown(result)
        else:
            st.error(f"Error: {response.status_code}, {response.text}")
else:
    st.caption("👆 Enter DAX and click the button to begin.")
