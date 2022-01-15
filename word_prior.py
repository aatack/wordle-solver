from typing import Callable, Iterator, List

import matplotlib.pyplot as plt

from letter_prior import ALPHABET, LetterPrior


class WordPrior:
    @staticmethod
    def prior(vocabulary: Callable[[], Iterator[str]], length: int = 5) -> "WordPrior":
        return WordPrior([LetterPrior.prior(vocabulary, i) for i in range(length)])

    def __init__(self, letter_priors: List[LetterPrior]):
        self._letter_priors = letter_priors

    def normalise(self):
        for prior in self._letter_priors:
            prior.normalise()

    def plot(self):
        _, axes = plt.subplots(len(self._letter_priors), sharex=True)
        for prior, axis in zip(self._letter_priors, axes):
            axis.plot(list(ALPHABET), [prior[letter] for letter in ALPHABET])
        plt.show()
