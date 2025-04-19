import streamlit as st
import requests
import os
import toml

# Constants
SECRETS_PATH = r"E:\python_DS\dax-sql\.streamlit\secrets.toml"
OPENROUTER_API_URL = "https://api.openrouter.ai/v1/chat/completions"  # Updated URL

def load_api_key():
    """Load the API key from secrets.toml or environment variables."""
    if os.path.exists(SECRETS_PATH):
        secrets = toml.load(SECRETS_PATH)
        return secrets.get("OPENROUTER_API_KEY")
    return os.getenv("OPENROUTER_API_KEY")

def validate_api_key(api_key):
    """Validate the API key and stop execution if missing or invalid."""
    if not api_key:
        st.error("API key for OpenRouter is missing. Please set it in the secrets.toml file or as an environment variable.")
        st.stop()
    if not isinstance(api_key, str) or len(api_key.strip()) == 0:
        st.error("Invalid API key format. Please check your API key.")
        st.stop()

def build_prompt(dax_input):
    """Build the prompt for the OpenRouter API."""
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

def call_openrouter_api(api_key, prompt):
    """Call the OpenRouter API with the given prompt."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "nvidia/llama-3.1-nemotron-ultra-253b-v1:free",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500,
        "temperature": 0.2
    }
    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error("A connection error occurred. Please check your internet connection or DNS settings.")
    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP error occurred: {e.response.status_code} - {e.response.reason}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while connecting to the API: {e}")
    return None

def display_result(response_json):
    """Display the result from the API response."""
    if response_json:
        result = response_json.get('choices', [{}])[0].get('message', {}).get('content', '').strip()
        if result:
            st.markdown("### 💬 Result")
            st.markdown(result)
        else:
            st.error("The API response was successful but did not contain any result. Please verify your input or try again later.")
    else:
        st.error("Failed to retrieve a valid response from the API.")

def main():
    """Main function to run the Streamlit app."""
    st.title("🧠 DAX to SQL Translator + Explainer using OpenRouter")
    st.markdown("""
    Paste any DAX expression below and get:
    - A plain English explanation
    - An SQL translation (if possible)
    - Any context-related warnings
    """)

    api_key = load_api_key()
    validate_api_key(api_key)

    dax_input = st.text_area("🔤 Enter your DAX formula here", height=200)

    if st.button("🧠 Translate & Explain") and dax_input.strip():
        with st.spinner("Thinking..."):
            prompt = build_prompt(dax_input)
            response_json = call_openrouter_api(api_key, prompt)
            display_result(response_json)
    else:
        st.caption("👆 Enter DAX and click the button to begin.")

if __name__ == "__main__":
    main()
