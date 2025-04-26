import streamlit as st
import requests
import os
import toml
import google.generativeai as genai

# Constants
SECRETS_PATH = r"E:\python_DS\dax-sql\.streamlit\secrets.toml"
OPENROUTER_API_URL = "https://api.openrouter.ai/v1/chat/completions"

# === Load Keys ===
def load_keys():
    if os.path.exists(SECRETS_PATH):
        secrets = toml.load(SECRETS_PATH)
        return {
            "gemini": secrets.get("GEMINI_API_KEY"),
            "openrouter": secrets.get("OPENROUTER_API_KEY")
        }
    return {
        "gemini": os.getenv("GEMINI_API_KEY"),
        "openrouter": os.getenv("OPENROUTER_API_KEY")
    }

# === Prompt Builder ===
def build_prompt(dax_input):
    return f"""
You are an expert in DAX and SQL.

Given the following DAX formula:

{dax_input}

Please:
1. Explain in plain English what this DAX measure or expression is doing.
2. Translate it to a SQL equivalent query, assuming relational database structure.
3. Point out any limitations where SQL can't fully mimic DAX behavior, especially due to evaluation or filter context.

Be concise and helpful.
"""

# === Gemini Handler ===
def call_gemini_api(api_key, prompt):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        st.error(f"Gemini error: {e}")
        return None

# === OpenRouter Handler ===
def call_openrouter_api(api_key, prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "nvidia/llama-3.1-nemotron-ultra-253b-v1:free",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 2000,
        "temperature": 0.2
    }
    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        return response.json().get('choices', [{}])[0].get('message', {}).get('content', '').strip()
    except requests.exceptions.RequestException as e:
        st.error(f"OpenRouter error: {e}")
        return None

# === Main App ===
def main():
    st.title("🧠 DAX to SQL Translator + Explainer")
    st.markdown("Paste any DAX formula to get its explanation and SQL translation.")

    # Model Selector
    model_choice = st.selectbox("🧪 Choose Model", ["Gemini", "OpenRouter"])
    keys = load_keys()
    api_key = keys.get(model_choice.lower())

    if not api_key:
        st.error(f"{model_choice} API key missing. Please set it in the secrets.toml or as env variable.")
        st.stop()

    dax_input = st.text_area("🔤 Enter your DAX formula", height=200)

    if st.button("🧠 Translate & Explain") and dax_input.strip():
        with st.spinner("Thinking..."):
            prompt = build_prompt(dax_input)
            if model_choice == "Gemini":
                result = call_gemini_api(api_key, prompt)
            else:
                result = call_openrouter_api(api_key, prompt)

            if result:
                st.markdown("### 💬 Result")
                st.markdown(result)
            else:
                st.error("No response received. Please try again.")

if __name__ == "__main__":
    main()
