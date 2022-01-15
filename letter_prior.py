from collections import defaultdict
from math import log
from random import uniform
from typing import Callable, Dict, Iterator

import matplotlib.pyplot as plt

from parameters import ALPHABET, INFERENCE_FACTOR


class LetterPrior:
    @staticmethod
    def prior(vocabulary: Callable[[], Iterator[str]], index: int) -> "LetterPrior":
        counts = {letter: 0.0 for letter in ALPHABET}
        for word in vocabulary():
            counts[word[index]] += 1
        total = sum(counts.values())
        prior = LetterPrior({letter: count / total for letter, count in counts.items()})
        prior.normalise()
        return prior

    def __str__(self) -> str:
        return "".join(sorted(ALPHABET, key=lambda l: self[l]))

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
        return sum(-p * log(p) for p in self._probabilities.values() if p > 0.0)

    def feedback_black(self, letter: str, hard: bool):
        if hard:
            self._probabilities[letter] = 0.0
        else:
            self._probabilities[letter] /= INFERENCE_FACTOR
            self.normalise()

    def feedback_yellow(self, letter: str):
        # NOTE: called for a yellow in a different position; yellows in this position
        #       will actually lead to a black feedback given to this prior
        self._probabilities[letter] *= INFERENCE_FACTOR
        self.normalise()

    def feedback_green(self, letter: str):
        self._probabilities = {
            _letter: (1.0 if _letter == letter else 0.0) for _letter in ALPHABET
        }

    def sample(self) -> str:
        threshold = uniform(0, 1)
        cumulative = 0.0
        for letter in ALPHABET:
            cumulative += self[letter]
            if cumulative >= threshold:
                return letter
        return "z"

    def merge(self, other: "LetterPrior"):
        for letter in ALPHABET:
            if letter not in self._probabilities:
                self._probabilities[letter] = 0.0
            self._probabilities[letter] += other[letter]
