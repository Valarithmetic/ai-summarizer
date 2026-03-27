# Getting Started with Streamlit — A Beginner's Toolkit

**Moringa AI Capstone | Prompt-Powered Kickstart**

---

## 1. Title & Objective

**Technology chosen:** Streamlit — a Python library for building web apps

**Why I chose it:**
Streamlit lets you build real, interactive AI-powered web applications using
only Python, with no HTML or JavaScript knowledge needed. It's widely used
in the AI/ML industry to demo models and tools quickly.

**End goal:**
Build and run a working AI Text Summarizer web app that takes any text as
input and returns an AI-generated summary using the Groq API.

---

## 2. Quick Summary of the Technology

**What is Streamlit?**
Streamlit is an open-source Python library that turns Python scripts into
shareable web apps in minutes. You write pure Python — no frontend skills
required — and Streamlit handles the UI rendering automatically.

**Where is it used?**

- Data science teams demoing ML models
- AI engineers building internal tools
- Students and researchers sharing interactive projects

**Real-world example:**
Hugging Face uses Streamlit-style interfaces to let users interact with
AI models directly in the browser without writing any frontend code.

---

## 3. System Requirements

- **OS:** Windows / macOS / Linux
- **Python:** 3.8 or higher (this project uses Python 3.13)
- **Editor:** VS Code (recommended)
- **Packages:**
  - `streamlit`
  - `groq`
  - `python-dotenv`
- **Accounts needed:** Groq account (free) for API key at console.groq.com

---

## 4. Installation & Setup Instructions

### Step 1 — Create your project folder

```bash
mkdir ai-summarizer
cd ai-summarizer
```

### Step 2 — Install required packages

```bash
pip install streamlit groq python-dotenv
```

### Step 3 — Add your API key

Create a file named `.env` in the project folder:

```
GROQ_API_KEY=your-groq-key-here
```

> Get your free key at: https://console.groq.com

### Step 4 — Create requirements.txt

```
streamlit
groq
python-dotenv
```

### Step 5 — Run the app

```bash
streamlit run app.py
```

Expected output: Browser opens at `localhost:8501` showing your app.

---

## 5. Minimal Working Example

**What it does:**
The user pastes any text, selects a summary length (short/medium/detailed),
clicks "Summarize", and the app calls the Groq API and displays the result.

**Code (app.py):**

```python
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

user_text = st.text_area(
    label="Your text",
    placeholder="Paste an article, paragraph, or any text here...",
    height=200
)

length_option = st.selectbox(
    label="Summary length",
    options=["Short (1-2 sentences)", "Medium (a short paragraph)",
             "Detailed (key points listed)"]
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
```

**Expected output:**
A browser-based web app where the user can paste text, choose summary
length, and receive an AI-generated summary within a few seconds.

---

## 6. AI Prompt Journal

| #   | Prompt Used                                                      | Where              | Response Summary                                                                        | Helpful?                                                    |
| --- | ---------------------------------------------------------------- | ------------------ | --------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 1   | "What is Streamlit and why is it good for AI projects?"          | Claude (claude.ai) | Explained Streamlit as a Python-only web framework popular in ML/AI demos               | Very helpful — gave me clear context before starting        |
| 2   | "Show me how to install Streamlit and create a Hello World app"  | Claude             | Provided pip install command and a 3-line starter app                                   | Helpful — got me running in minutes                         |
| 3   | "How do I connect the Groq API to a Streamlit app?"              | Claude             | Showed how to use python-dotenv to load API keys safely and structure the API call      | Very helpful — explained the security reason for .env files |
| 4   | "What does st.spinner() do and when should I use it?"            | Claude             | Explained it shows a loading animation while waiting for slow operations like API calls | Helpful — improved the user experience                      |
| 5   | "How do I handle errors if the API call fails?"                  | Claude             | Showed try/except pattern and st.error() for displaying friendly error messages         | Very helpful — taught me defensive coding                   |
| 6   | "The model llama3-8b-8192 is decommissioned, what should I use?" | Claude             | Suggested llama-3.3-70b-versatile as the replacement model                              | Very helpful — fixed the error immediately                  |

**Reflection:**
Using AI to learn Streamlit significantly sped up my setup process. Instead
of reading through full documentation, I could ask targeted questions and
get working code examples immediately. The most valuable prompts were the
ones where I asked "why" not just "how" — understanding the reason behind
using .env files taught me about API key security, not just syntax. When
errors came up, AI helped me debug and fix them faster than searching through
documentation alone.

---

## 7. Common Issues & Fixes

| Error                                | Cause                      | Fix                                        |
| ------------------------------------ | -------------------------- | ------------------------------------------ |
| `'streamlit' is not recognized`      | Streamlit not installed    | Run `pip install streamlit` again          |
| `insufficient_quota`                 | OpenAI has no free tier    | Switch to Groq API which is free           |
| `model decommissioned`               | llama3-8b-8192 was removed | Use `llama-3.3-70b-versatile` instead      |
| `'git' is not recognized`            | Git not installed          | Download from git-scm.com and reinstall    |
| App doesn't reload after code change | Needs manual restart       | Press `Ctrl+C` then `streamlit run app.py` |

---

## 8. References

- [Streamlit official docs](https://docs.streamlit.io)
- [Groq API docs](https://console.groq.com/docs)
- [python-dotenv docs](https://pypi.org/project/python-dotenv/)
- [Streamlit — Getting Started](https://docs.streamlit.io/get-started)
- [Groq supported models](https://console.groq.com/docs/models)
- [StackOverflow — Streamlit tag](https://stackoverflow.com/questions/tagged/streamlit)
