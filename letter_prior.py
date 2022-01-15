from typing import Dict

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class LetterPrior:
    def __init__(self, probabilities: Dict[str, float]):
        self._probabilities = probabilities

    def __getitem__(self, letter: str) -> float:
        assert len(letter) == 1 and letter in ALPHABET
        return self._probabilities.get(letter, 0.0)
