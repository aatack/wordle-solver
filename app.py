import streamlit as st

from solver import Solver

OPTIONS = ["Green", "Yellow", "Grey"]


if "solver" not in st.session_state:
    st.session_state.solver = Solver()

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

    block = st.empty()

    if block.button("Confirm"):
        block.empty()
        with st.spinner("Loading"):
            st.session_state.solver.guess(
                guess, [2 - OPTIONS.index(colour) for colour in colours]
            )

        st.experimental_rerun()

st.write("---")

st.write(str(st.session_state.solver.best_answer()))
with st.spinner("Loading best guess"):
    st.write(str(st.session_state.solver.best_entropy()))
