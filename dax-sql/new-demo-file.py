import streamlit as st
# import os
# import json
import requests
import random
import time

# === Constants ===
OPENROUTER_API_KEY = "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"  # 🔑 Replace this with your actual OpenRouter API key
MODEL_NAME = "deepseek/deepseek-r1-0528:free"

# === Build prompt ===
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

# === Call DeepSeek via OpenRouter ===
def call_deepseek(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are an expert in DAX and SQL."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 1024
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    else:
        return f"❌ Error {response.status_code}: {response.text}"

# === Main App ===
def main():
    st.set_page_config(page_title="DAX Decode", page_icon="🤖", layout="wide")
    st.title("🤖 DAX to SQL Translator + Explainer")
    st.caption("Built with Python + DeepSeek via OpenRouter")

    # Initialize chat history
    if "history" not in st.session_state:
        st.session_state.history = []

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

    if st.button("🚀 Translate & Explain") and dax_input.strip():
        with st.spinner(random.choice([
            "Cooking up the best SQL...",
            "Reading DAX secrets...",
            "Assembling SQL magic...",
            "Thinking hard... 🤔",
            "Converting logic to SQL wisdom..."
        ])):
            prompt = build_prompt(dax_input)
            result = call_deepseek(prompt)

            # Split explanation and SQL
            if "\n\n" in result:
                explanation, sql_query = result.split('\n\n', 1)
            else:
                explanation, sql_query = result, ""

            # Add to history
            st.session_state.history.append({
                "dax": dax_input,
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
                st.text_area(f"📋 Copy SQL for {i}", value=entry['sql'], key=f"copy_{i}", height=100)
                st.button("🗑️ Clear This", key=f"clear_{i}", on_click=lambda: st.session_state.history.remove(entry))

    # Show chat history
    # if st.session_state.history:
    #     for i, entry in enumerate(reversed(st.session_state.history), 1):
    #         st.markdown(f"### 📝 Query {i}")
    #         st.markdown(f"**DAX:** `{entry['dax']}`")
    #         st.markdown(f"**Explanation:** {entry['explanation']}")
    #         st.markdown("**SQL Query:**")
    #         st.code(entry['sql'], language='sql')
    #         st.button("🗑️ Clear This", key=f"clear_{i}", on_click=lambda: st.session_state.history.remove(entry))

    st.markdown("---")
    st.caption("Made with ❤️ using Python + OpenRouter + DeepSeek")

if __name__ == "__main__":
    main()
