import streamlit as st
import re
import google.generativeai as genai
from tools import get_random_joke, translate_text, search_joke_by_topic
from build_prompt import build_mcp_prompt

system = "You are an assistant who only tells offensive, sarcastic, and vulgar jokes using search_joke_by_topic tool."
tools = "search_joke_by_topic(topic): Fetches offensive/sarcastic jokes based on a topic."

if "memory" not in st.session_state:
    st.session_state.memory = []

st.set_page_config(page_title="Offensive Joke Bot 😜", page_icon="😜")
st.title("😜 Offensive Joke Generator")
st.write("Ask me something sarcastic, rude, or just plain offensive. You've been warned.")

user_api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

if not user_api_key:
    st.sidebar.warning("Please enter your Gemini API Key to continue.")
    st.stop()

model_options = [
    "gemini-1.5-pro",
    "gemini-1.5-flash",
    "gemini-pro",
    "gemini-1.5-flash-vision",
    "gemini-1.5-pro-vision",
    "gemini-2.0-flash-lite",
]
selected_model = st.sidebar.selectbox("Choose Gemini Model", model_options, index=1)

try:
    genai.configure(api_key=user_api_key)
    model = genai.GenerativeModel(selected_model)

    test_response = model.generate_content("Hello!")


    if not hasattr(test_response, "text") or not test_response.text:
        st.sidebar.error("Invalid API key.")
        st.stop()


except Exception as e:
    st.sidebar.error(f"API error: {e}")
    st.stop()


#language selector
selected_language = st.selectbox("Choose the language for your joke:", [
    "english", "spanish", "french", "german", "hindi", "japanese", "nepali", "chinese", "russian"
])


# Function to convert language name to ISO code
lang_map = {
    "english": "en",
    "spanish": "es",
    "french": "fr",
    "german": "de",
    "hindi": "hi",
    "japanese": "ja",
    "nepali": "ne",
    "chinese": "zh",
    "russian": "ru",
}


def handle_tool_call(topic, target_lang_code="en"):
    try:
      
        joke = search_joke_by_topic(topic)

        # if not joke:
        #     joke = get_random_joke()

         # Detect placeholder or known "not found" messages
        if (
            joke is None or 
            not joke.strip() or 
            "no jokes" in joke.lower() or 
            "not found" in joke.lower()
        ):

            raise ValueError("Joke search failed or returned no joke.")


        translated = translate_text(joke, target_lang_code)

        if not translated or not translated.strip():
            raise ValueError("Translation failed.")

        st.success("searching🔍🔍")
        return joke, translated
        
    
    except Exception as e:
        try:
            fallback = get_random_joke()
            st.write("Searching failed. Generating random joke🔍🔍")

            translated = translate_text(fallback, target_lang_code)

            if not translated or not translated.strip():
                raise ValueError("Translation failed.")


            return fallback, translated
        
        except Exception as inner_e:
            return f"Error: {e}\n also failed fallback: {inner_e}", None


user_input = st.text_input("Enter a topic to generate a sarcastic joke about:")

if user_input:
    prompt = build_mcp_prompt(system, tools, user_input, st.session_state.memory)

    target_lang_code = lang_map.get(selected_language.lower(),"en")

    original_joke, translated_joke = handle_tool_call(user_input, target_lang_code)

    if translated_joke:
        st.markdown("!🤡 Original Joke (English)")
        st.write(original_joke)
        st.markdown(f"!🌎 Joke in {selected_language.capitalize()} ")
        st.write(translated_joke)


        st.session_state.memory.append(f"user:{user_input}")
        st.session_state.memory.append(f"AI:{translated_joke}")
    
    else:
        st.error(original_joke)
        st.session_state.memory.append(f"Unlucky AI:{original_joke}")

        

with st.expander("Conversation History"):
    for line in st.session_state.memory:
        st.markdown(f"- {line}")
