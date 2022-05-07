import streamlit as st

OPTIONS = ["Green", "Yellow", "Grey"]


class A:
    def __init__(self):
        self.x = 0


if "A" not in st.session_state:
    st.session_state["A"] = A()

st.latex(st.session_state.A.x)

st.write("# Wordle Solver")

st.write(
    "Test app for working out how to use Streamlit, and also to provide a nicer "
    "UI for the Wordle bot I wrote a few months ago."
)

st.write(f"Current random state: {st.session_state.get('random', 0)}")

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
            import random

            print(guess, [2 - OPTIONS.index(colour) for colour in colours])
            st.session_state.random = random.randint(1, 100)

        st.session_state.A.x += 1
        st.experimental_rerun()

    st.write("---")
