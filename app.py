import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Text Summarizer", page_icon="📝")
st.title("📝 AI Text Summarizer")
st.write("Paste any text below and get an AI-generated summary instantly.")

# User inputs
user_text = st.text_area(
    label="Your text",
    placeholder="Paste an article, paragraph, or any text here...",
    height=200
)

length_option = st.selectbox(
    label="Summary length",
    options=["Short (1-2 sentences)", "Medium (a short paragraph)", "Detailed (key points listed)"]
)

if st.button("Summarize"):
    if not user_text.strip():
        st.warning("Please paste some text first!")
    else:
        length_instructions = {
            "Short (1-2 sentences)": "Summarize this in 1-2 sentences only.",
            "Medium (a short paragraph)": "Summarize in 3-5 sentences.",
            "Detailed (key points listed)": "Summarize as bullet points."
        }
        instruction = length_instructions[length_option]

        with st.spinner("Summarizing..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that summarizes text clearly."},
                        {"role": "user", "content": f"{instruction}\n\nText:\n{user_text}"}
                    ]
                )
                summary = response.choices[0].message.content
                st.success("Done!")
                st.subheader("Summary")
                st.write(summary)
                st.text_area("Copy your summary", value=summary, height=100)

            except Exception as e:
                st.error(f"Something went wrong: {e}")