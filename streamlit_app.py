import streamlit as st
import requests


def fetch_word_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    return response.json()


def display_word_definitions(definitions):
    for entry in definitions:
        word = entry["word"]
        st.markdown(f"**{word}**")
        
        for definition in entry["meanings"]:
            part_of_speech = definition["partOfSpeech"]
            st.markdown(f"**{part_of_speech}**:")
            
            for i, d in enumerate(definition["definitions"], start=1):
                st.write(f"{i}. {d['definition']}")
                if "example" in d:
                    st.write(f"   *Example: {d['example']}")
            
            st.write("---")


# Streamlit app
def main():
    st.title("Word Definitions")
    
    word = st.text_input("Enter a word:")
    if st.button("Get Definitions"):
        if word:
            definitions = fetch_word_definition(word)
            if definitions:
                display_word_definitions(definitions)
            else:
                st.write("No definitions found for the given word.")
        else:
            st.write("Please enter a word to get definitions.")
