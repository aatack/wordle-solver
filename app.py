import streamlit as st

# st.set_page_config(layout="wide")

st.write("# Wordle Solver")

st.write(
    "Test app for working out how to use Streamlit, and also to provide a nicer "
    "UI for the Wordle bot I wrote a few months ago."
)


with st.empty():
    guess = st.text_input("Guess", max_chars=5)

    if len(guess) > 0:
        with st.container():
            columns = st.columns([1] * len(guess))

            for i, (column, character) in enumerate(zip(columns, guess)):
                column.button(character, key=str(i))
