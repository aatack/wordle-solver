from collections import defaultdict
from typing import Callable, Dict, Iterator

import matplotlib.pyplot as plt

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class LetterPrior:
    @staticmethod
    def prior(vocabulary: Callable[[], Iterator[str]], index: int) -> "LetterPrior":
        counts = defaultdict(lambda: 0)
        for word in vocabulary():
            counts[word[index]] += 1
        total = sum(counts.values())
        return LetterPrior({letter: count / total for letter, count in counts.items()})

    def __init__(self, probabilities: Dict[str, float]):
        self._probabilities = probabilities

    def __getitem__(self, letter: str) -> float:
        assert len(letter) == 1 and letter in ALPHABET
        return self._probabilities.get(letter, 0.0)

    def normalise(self):
        magnitude = sum(self._probabilities.values())
        for letter in self._probabilities:
            self._probabilities[letter] /= magnitude

    def plot(self):
        plt.plot(list(ALPHABET), [self[letter] for letter in ALPHABET])
        plt.show()
