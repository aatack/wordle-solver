import streamlit as st

from solver import Solver

OPTIONS = ["Green", "Yellow", "Grey"]


if "solver" not in st.session_state:
    st.session_state.solver = Solver()

solver = st.session_state.solver

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
            solver.guess(guess, [2 - OPTIONS.index(colour) for colour in colours])

        st.experimental_rerun()

st.write("---")

left, middle, right = st.columns(3)

try:
    with left:
        st.metric("Guesses made", solver.guesses_made)

    with middle:
        try:
            answer, probability = solver.best_answer()
            st.metric(
                "Highest probability",
                answer,
                f"{probability * 100:.1f}%",
                delta_color="off",
            )
        except ZeroDivisionError:
            st.success("Success")

    with right:
        try:
            with st.spinner("Loading best guess"):
                option, entropy = solver.best_entropy()
                st.metric(
                    "Highest information",
                    option,
                    f"{(1 - entropy) * 100:.1f}",
                    delta_color="off",
                )
        except ZeroDivisionError:
            if probability >= 0.999:
                st.success("The word has been found")
            else:
                st.error("The word is not in the vocabulary list")

            if st.button("Reset"):
                st.session_state.clear()
                st.experimental_rerun()

except AssertionError as e:
    # Normally this is because the state has been invalidated by a reload
    print("Caught assertion error:", e)

    st.session_state.clear()
    st.experimental_rerun()

# Still to do:
# - Tidy up this file
# - Add plots of the historical data (letter/word distributions, etc.)
