# 🤖 TalentScout – AI Hiring Assistant

TalentScout is an intelligent AI-powered hiring assistant built using **Streamlit** and **Groq's LLaMA 3** models. It helps HR teams automate technical screening by asking role-specific questions and providing expert-grade answers.

---

## 🚀 Features

- 📋 **Smart Candidate Form** – Collects all essential details from the applicant.
- 🧠 **Dynamic Tech Questions** – Generates 3-5 technical questions for each tech skill listed.
- 💬 **Interactive Chat Interface** – Ask follow-up queries and get professional answers instantly.
- ✅ **Answer Generation** – Automatically answers technical questions using LLaMA-3.
- 🔐 **Exit Handling** – Gracefully ends the chat when user types "exit" or "quit".

---

## 📂 Folder Structure

```
TalentScout_Chatbot/
├── app.py              # Main Streamlit application
├── prompts.py          # Logic to generate technical questions
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📦 Installation

```bash
git clone <your-repo-url>
cd TalentScout_Chatbot
pip install -r requirements.txt
```

---

## 🏃 Run the App

```bash
streamlit run app.py
```

Make sure your `Groq` API key is correctly set in `prompts.py` and `app.py`.

---

## 🔐 API Key Setup

```python
from groq import Groq
client = Groq(api_key="your_groq_api_key")
```

---

## 📬 Contact

For queries or enhancements, feel free to reach out:
**Name:** Pushpendra Singh Bhadauriya  
**Email:** pushpendrabhadauriya28@gmail.com


