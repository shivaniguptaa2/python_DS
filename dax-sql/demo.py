import streamlit as st
import requests
import os
import toml

# === Constants ===
SECRETS_PATH = r"E:\python_DS\dax-sql\.streamlit\secrets.toml"
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

# === Load API Key ===
def load_api_key():
    """Load Mistral API key."""
    if os.path.exists(SECRETS_PATH):
        secrets = toml.load(SECRETS_PATH)
        return secrets.get("MISTRAL_API_KEY")
    return os.getenv("MISTRAL_API_KEY")

# === Build Prompt ===
def build_prompt(dax_input):
    """Create prompt for DAX explanation and SQL conversion."""
    return f"""
You are an expert in DAX and SQL.

Given the following DAX formula:

{dax_input}

Please:
1. Translate it into an equivalent SQL query, assuming a relational database structure.

Be clear, concise, and professional.
"""

# === Call Mistral API ===
def call_mistral_api(api_key, prompt):
    """Send the prompt to Mistral and fetch the result."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-small",  # you can change to mistral-medium or mistral-large if needed
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "top_p": 0.95,
        "max_tokens": 2000,
        "stream": False
    }
    try:
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        return response.json().get('choices', [{}])[0].get('message', {}).get('content', '').strip()
    except requests.exceptions.RequestException as e:
        st.error(f"Mistral API error: {e}")
        return None

# === Main App ===
def main():
    """Main Streamlit app."""
    st.title("🧠 DAX to SQL Translator + Explainer (Mistral API Direct)")
    st.markdown("Paste your DAX formula and get an English explanation and SQL translation.")

    api_key = load_api_key()
    if not api_key:
        st.error("Mistral API key missing. Please set it in the secrets.toml file or as an environment variable.")
        st.stop()

    dax_input = st.text_area("🔤 Enter your DAX formula", height=200)

    if st.button("🧠 Translate & Explain") and dax_input.strip():
        with st.spinner("Thinking..."):
            prompt = build_prompt(dax_input)
            result = call_mistral_api(api_key, prompt)

            if result:
                st.markdown("### 💬 Result")
                st.markdown(result)
            else:
                st.error("No response received. Please try again later.")

if __name__ == "__main__":
    main()
