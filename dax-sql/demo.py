import streamlit as st
import os
import json
import vertexai
from vertexai.preview.language_models import TextGenerationModel
import random
import time

# === Constants ===
SECRETS_PATH = r"E:\python_DS\dax-sql\key.json"  # Path to your service account JSON
PROJECT_ID = "YOUR_GCP_PROJECT_ID"
LOCATION = "us-central1"  # Change if your Vertex AI region is different

# === Load credentials ===
def load_credentials():
    if os.path.exists(SECRETS_PATH):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SECRETS_PATH
    else:
        st.error("Vertex AI credentials JSON not found!")
        st.stop()

# === Initialize Vertex AI ===
def init_vertex_ai():
    vertexai.init(project=PROJECT_ID, location=LOCATION)

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

# === Call Vertex AI ===
def call_vertex_ai(prompt):
    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        prompt,
        max_output_tokens=1024,
        temperature=0.2
    )
    return response.text.strip()

# === Main App ===
def main():
    st.set_page_config(page_title="DAX Decode", page_icon="🤖", layout="wide")
    st.title("🤖 DAX to SQL Translator + Explainer")
    st.caption("Built with Python + Vertex AI")

    load_credentials()
    init_vertex_ai()

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
            "Decoding DAX with AI...",
            "Thinking in SQL...",
            "Translating logic...",
            "Generating query..."
        ])):
            prompt = build_prompt(dax_input)
            result = call_vertex_ai(prompt)

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

    # Show chat history
    if st.session_state.history:
        for i, entry in enumerate(reversed(st.session_state.history), 1):
            st.markdown(f"### 📝 Query {i}")
            st.markdown(f"**DAX:** `{entry['dax']}`")
            st.markdown(f"**Explanation:** {entry['explanation']}")
            st.markdown("**SQL Query:**")
            st.code(entry['sql'], language='sql')
            st.button("🗑️ Clear This", key=f"clear_{i}", on_click=lambda: st.session_state.history.remove(entry))

    st.markdown("---")
    st.caption("Made with ❤️ using Python + Vertex AI")

if __name__ == "__main__":
    main()
