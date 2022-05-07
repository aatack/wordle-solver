import streamlit as st

OPTIONS = ["Green", "Yellow", "Grey"]

st.write("# Wordle Solver")

st.write(
    "Test app for working out how to use Streamlit, and also to provide a nicer "
    "UI for the Wordle bot I wrote a few months ago."
)

st.write("---")
guess = st.text_input("Word entered", "", max_chars=5).lower()

if len(guess) == 5:
    st.write("---")

    columns = st.columns(5)
    colours = [
        column.radio(character.upper(), OPTIONS, index=2, key=str(i))
        for i, (column, character) in enumerate(zip(columns, guess))
    ]
