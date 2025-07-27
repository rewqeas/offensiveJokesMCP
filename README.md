# offensiveJokesMCP
# 😜 Offensive Joke Generator

A dark-humored Streamlit app that uses Google Gemini and joke APIs to deliver sarcastic, offensive, and vulgar jokes based on your chosen topic — with multilingual support!

> ⚠️ **Warning:** This app is intended for mature audiences. The jokes generated may be offensive, vulgar, or inappropriate. Use at your own discretion.

---

## 🚀 Features

- 🤖 Generates sarcastic or offensive jokes based on user input (topic).
- 🌐 Translates the jokes into various languages (e.g., Spanish, German, Hindi, Nepali).
- 🔁 Falls back to a random joke if no joke is found for a specific topic.
- 🧠 Remembers past conversation history.
- 🔐 Supports Gemini API key input for dynamic model selection.

---

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/) — for the web UI.
- [Google Gemini](https://ai.google.dev/) — for language model capabilities.
- Public joke APIs (custom or open-source).
- LibreTranslate (or alternative) — for language translation.
- Python (backend logic and tool integration).

---

## 📦 Installation

```bash
git clone https://github.com/rewqeas/offensiveJokesMCP.git
cd offensiveJokesMCP
pip install -r requirements.txt
streamlit run app.py
