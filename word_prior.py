from copy import deepcopy
from os import P_OVERLAY
from random import uniform
from typing import Callable, Iterator, List, Optional, Set, Tuple

import matplotlib.pyplot as plt
from tqdm import tqdm

from feedback import generate_feedback
from letter_prior import LetterPrior
from parameters import ALPHABET, Colours


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

    def __str__(self) -> str:
        return "\n".join(str(prior) for prior in self._letter_priors)

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
                for prior in self._letter_priors:
                    prior.feedback_black(letter, hard=True)

            elif colour == Colours.YELLOW:
                for i, prior in enumerate(self._letter_priors):
                    if i == index:
                        prior.feedback_black(letter, hard=True)
                    else:
                        prior.feedback_yellow(letter)

            elif colour == Colours.GREEN:
                self._letter_priors[index].feedback_green(letter)

            else:
                raise ValueError("Invalid colour")

    def sample(self) -> str:
        return "".join(prior.sample() for prior in self._letter_priors)

    def copy(self) -> "WordPrior":
        return deepcopy(self)

    def merge(self, other: "WordPrior"):
        for left, right in zip(self._letter_priors, other._letter_priors):
            left.merge(right)

    def posterior(self, guess: str, answers: List[str]) -> "WordPrior":
        posterior: Optional[WordPrior] = None

        for answer in answers:
            copy = self.copy()
            copy.feedback(guess, generate_feedback(guess, answer))
            if posterior is None:
                posterior = copy
            else:
                posterior.merge(copy)

        posterior.normalise()
        return posterior

    def entropy_ratio(self, guess: str, answers: List[str]) -> float:
        return self.posterior(guess, answers).total_entropy / self.total_entropy

    def best_guess_minimise_entropy(
        self, vocabulary: "Vocabulary"
    ) -> Tuple[str, float]:
        count = 50

        answers = vocabulary.sample(count, self)
        guesses = vocabulary.uniform_sample(count)

        ratios = [(word, self.entropy_ratio(word, answers)) for word in tqdm(guesses)]
        return min(ratios, key=lambda p: p[1])

    def best_guess_guess_answer(self, vocabulary: "Vocabulary") -> Tuple[str, float]:
        word = max(vocabulary.all_words(), key=lambda word: self[word])
        return word, self[word]
