import streamlit as st

OPTIONS = ["Green", "Yellow", "Grey"]

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
            import time

            time.sleep(1)
            st.session_state.random = random.randint(1, 100)
            block.info("Finished")

        time.sleep(1)
        st.experimental_rerun()
