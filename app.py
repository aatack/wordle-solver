import streamlit as st

# st.set_page_config(layout="wide")

st.write("# Wordle Solver")

st.write(
    "Test app for working out how to use Streamlit, and also to provide a nicer "
    "UI for the Wordle bot I wrote a few months ago."
)


def store_guess(g: str):
    print("Storing", g)
    st.session_state.guess = g


guess = st.session_state.guess if "guess" in st.session_state else ""

if len(guess) < 5:
    update = st.text_input(label="", value=guess, max_chars=5)
    print("Guessed:", update)
    if update != guess:
        st.session_state.guess = update
        # Only needed if the state up to this point wants to be updated?
        st.experimental_rerun()


if len(guess) == 5:
    columns = st.columns(len(guess))

    for i, (column, character) in enumerate(zip(columns, guess)):
        column.button(character, key=str(i))

    def reset_guess():
        st.session_state.guess = ""

    st.button("Reset", on_click=reset_guess)
