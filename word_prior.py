from typing import Callable, Iterator, List

import matplotlib.pyplot as plt

from letter_prior import LetterPrior
from parameters import ALPHABET


class Colours:
    BLACK = 0
    YELLOW = 1
    GREEN = 2


class WordPrior:
    @staticmethod
    def prior(vocabulary: Callable[[], Iterator[str]], length: int = 5) -> "WordPrior":
        return WordPrior([LetterPrior.prior(vocabulary, i) for i in range(length)])

    def __init__(self, letter_priors: List[LetterPrior]):
        self._letter_priors = letter_priors

    def __getitem__(self, word: str) -> float:
        probability = 1.0
        for letter, prior in zip(word, self._letter_priors):
            probability *= prior[letter]
        return probability

    def normalise(self):
        for prior in self._letter_priors:
            prior.normalise()

    def plot(self):
        _, axes = plt.subplots(len(self._letter_priors), sharex=True)
        for prior, axis in zip(self._letter_priors, axes):
            axis.plot(list(ALPHABET), [prior[letter] for letter in ALPHABET])
        plt.show()

    @property
    def total_entropy(self) -> float:
        return sum(prior.entropy for prior in self._letter_priors)

    def feedback(self, word: str, colours: List[int]):
        for index, (letter, colour) in enumerate(zip(word, colours)):
            if colour == Colours.BLACK:
                self._letter_priors[index].feedback_black(letter)

            elif colour == Colours.YELLOW:
                for i, prior in enumerate(self._letter_priors):
                    if i == index:
                        prior.feedback_black(letter)
                    else:
                        prior.feedback_yellow(letter)

            elif colour == Colours.GREEN:
                self._letter_priors[index].feedback_green(letter)

            else:
                raise ValueError("Invalid colour")