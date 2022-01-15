from collections import defaultdict
from math import log
from typing import Callable, Dict, Iterator

import matplotlib.pyplot as plt

from parameters import ALPHABET, INFERENCE_FACTOR


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

    @property
    def entropy(self) -> float:
        return sum(-p * log(p) for p in self._probabilities.values())

    def feedback_black(self, letter: str):
        del self._probabilities[letter]

    def feedback_yellow(self, letter: str):
        # NOTE: called for a yellow in a different position; yellows in this position
        #       will actually lead to a black feedback given to this prior
        self._probabilities[letter] *= INFERENCE_FACTOR

    def feedback_green(self, letter: str):
        letters = set(self._probabilities.keys())
        letters.remove(letter)
        for _letter in letters:
            del self._probabilities[_letter]
