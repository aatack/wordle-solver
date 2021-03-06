from typing import Iterator

from solver.parameters import Colours


def generate_feedback(guess: str, answer: str) -> Iterator[str]:
    # TODO: generate parser for observed -> internal feedback

    for guess_letter, answer_letter in zip(guess, answer):
        if guess_letter == answer_letter:
            yield Colours.GREEN
        elif guess_letter in answer:
            yield Colours.YELLOW
        else:
            yield Colours.BLACK
