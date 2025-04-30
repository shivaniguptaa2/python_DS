import streamlit as st
import requests
import os
import toml
import random
import time

# Constants
SECRETS_PATH = r"E:\python_DS\dax-sql\.streamlit\secrets.toml"
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

# === Load API Key ===
def load_api_key():
    if os.path.exists(SECRETS_PATH):
        secrets = toml.load(SECRETS_PATH)
        return secrets.get("MISTRAL_API_KEY")
    return os.getenv("MISTRAL_API_KEY")

# === Prompt Builder ===
def build_prompt(dax_input):
    return f"""
You are an expert in DAX and SQL.

Given the following DAX formula:

{dax_input}

Please:
1. Explain in plain English what this DAX measure or expression is doing.
2. Translate it to a SQL equivalent query, assuming relational database structure.

Be concise and helpful.
"""

# === Mistral API Handler ===
def call_mistral_api(api_key, model, prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 20000,
        "temperature": 0.2
    }
    try:
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data, timeout=20)
        response.raise_for_status()
        return response.json().get('choices', [{}])[0].get('message', {}).get('content', '').strip()
    except requests.exceptions.RequestException as e:
        st.error(f"Mistral API error: {e}")
        return None

# === Main App ===
def main():
    st.set_page_config(page_title="DAX Decode", page_icon="🤖", layout="wide")
    st.title("🤖 DAX Decode")
    st.caption("Paste any DAX formula to get an English explanation and SQL translation.")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Load API Key
    api_key = load_api_key()
    if not api_key:
        st.error("Mistral API key missing! Please set it in your secrets.toml or environment variables.")
        st.stop()

    # DAX input
    st.markdown("### 🔤 Enter DAX Formula")
    sample_dax = st.selectbox(
        "Or pick a sample DAX to try 👇",
        [
            "",
            "Total Sales = SUM(Sales[Amount])",
            "Total Customers = DISTINCTCOUNT(Customer[CustomerID])",
            "Sales Growth % = DIVIDE(SUM(Sales[Amount]) - SUM(PreviousSales[Amount]), SUM(PreviousSales[Amount]))"
        ]
    )
    dax_input = st.text_area("✏️ Your DAX Input", value=sample_dax, height=200)

    # Translate button
    if st.button("🚀 Translate & Explain") and dax_input.strip():
        loading_msgs = [
            "Cooking up the best SQL...",
            "Reading DAX secrets...",
            "Assembling SQL magic...",
            "Thinking hard... 🤔",
            "Converting logic to SQL wisdom..."
        ]
        with st.spinner(random.choice(loading_msgs)):
            progress = st.progress(0)
            for i in range(0, 100, 5):
                time.sleep(0.03)
                progress.progress(i + 5)

            prompt = build_prompt(dax_input)
            result = call_mistral_api(api_key, "mistral-medium", prompt)

        if result:
            # Split response
            explanation, sql_query = result.split('\n\n', 1)
                        # Current output
            st.markdown("### 💬 Explanation")
            st.markdown(explanation)
            st.markdown("### 💻 SQL Query")
            st.code(sql_query.strip(), language='sql')

            # Save to chat history
            st.session_state.chat_history.append({
                "dax": dax_input.strip(),
                "explanation": explanation.strip(),
                "sql": sql_query.strip()
            })

        # Display chat history
    if st.session_state.chat_history:
        st.markdown("## 📚 Previous Translations")
        for i, entry in enumerate(reversed(st.session_state.chat_history), 1):
            with st.expander(f"{i}. {entry['dax']}"):
                st.markdown("**Explanation:**")
                st.markdown(entry['explanation'])
                st.markdown("**SQL Query:**")
                st.code(entry['sql'], language='sql')


    # Clear Output
    if st.button("🗑️ Clear Output"):
        st.session_state.chat_history = []
        # st.experimental_rerun()

    st.markdown("---")
    st.caption("Made with ❤️ by Shivani!")

if __name__ == "__main__":
    main()
