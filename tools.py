import requests
import random
from urllib.parse import urlencode #to convert dict to query string

#getting jokes from various APIs
def get_dad_jokes():
    try:
        headers = {"Accept": "text/plain"}
        res = requests.get("https://icanhazdadjoke.com/", headers=headers)
        if res.status_code == 200:
            return res.text.strip()
        else:
            return f"Error: Unable to fetch dad joke. Status code: {res.status_code}"
        
    except Exception as e:
        return f"Dad joke tool error: {str(e)}"
    

def get_official_joke():
    try:
        res = requests.get("https://official-joke-api.appspot.com/jokes/random")

        if res.status_code == 200:
            data = res.json()
            return f"{data['setup']} - {data['punchline']}"
        else:
            return f"Error: {res.status_code}-couldn't fetch official joke."
        
    except Exception as e:
        return f"Official joke tool error: {str(e)}"
    

def get_chunk_jokes_text():
    try:
        res = requests.get("https://api.chucknorris.io/jokes/random")

        if res.status_code == 200:
            return res.json().get("value", "No joke found.")
        
        else:
            return f"Error: Unable to fetch Chuck Norris joke. Status code: {res.status_code}"
        

    except Exception as e:
        return f"Chuck Norris joke tool error: {str(e)}"
    

def get_geek_joke_text():

    try:
        res = requests.get("https://geek-jokes.sameerkumar.website/api?format=text")

        if res.status_code == 200:
            return res.text.strip()
        
        else:
            return f"Error: Unable to fetch geek joke. Status code: {res.status_code}" 
        
    except Exception as e:
        return f"Geek joke tool error: {str(e)}"
    

def get_jokeapi_text():
    try:
        res = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")

        if res.status_code == 200:
            return res.json().get("joke", "No joke found.")

        else:
            return f"Error: Unable to fetch joke from JokeAPI. Status code: {res.status_code}"
        
    except Exception as e:
        return f"JokeAPI tool error: {str(e)}"
    

joke_sources = [
    get_dad_jokes,
    get_official_joke,
    get_chunk_jokes_text,
    get_geek_joke_text,
    get_jokeapi_text
]

def get_random_joke():
    joke_func = random.choice(joke_sources)

    try:
        return joke_func()
    except Exception as e:
        return f"Error fetching joke: {str(e)}"
    

#selecting language code based on language name

LANG_NAME_TO_CODE = {
    "english": "en",
    "spanish": "es",
    "french": "fr",
    "german": "de",
    "hindi": "hi",
    "nepali": "ne",
    "japanese": "ja",
    "arabic": "ar",
    "chinese": "zh",
    "italian": "it",
    "russian": "ru",
    "portuguese": "pt",
    "korean": "ko",
}

def get_language_code(language_name):
    lang = language_name.lower()
    return LANG_NAME_TO_CODE.get(lang,'en')#default english if others not found


#translator

def translate_text(text, target_lang):
    try:
        lang_code = f'en|{target_lang}'

        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": text,
            "langpair": lang_code,


        }
        res = requests.get(url,params=params)


        if res.status_code == 200:
            data = res.json()
            return data['responseData']['translatedText']
        
        else:
            return f"Error: Unable to translate text. Status code: {res.status_code}"
        
    except Exception as e:
        return f"Translation error: {str(e)}"
    

#search joke by topic
def search_joke_by_topic(topic):
    try:
        url = "https://icanhazdadjoke.com/search"
        headers = {"Accept": "application/json"}
        params = {"term":topic}

        res = requests.get(url, headers = headers, params = params)

        if res.status_code == 200:
            data = res.json()
            results = data.get("results", [])

            if results:
                # return a random joke from matching results
                return random.choice(results)['joke']
            
            else:
                return f"No jokes about '{topic}' found."
            
    except Exception as e:
        return f"Error searching for joke: {str(e)}"



