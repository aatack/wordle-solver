from typing import List, Tuple

from solver.vocabulary import Vocabulary, comprehensive
from solver.word_prior import WordPrior


class Solver:
    def __init__(self):
        # TODO: make hyperparameters out of which ones should be used here
        self.prior = WordPrior.prior(comprehensive)
        self.vocabulary = Vocabulary(set(comprehensive()))

        self.guesses_made = 0

    def guess(self, word: str, colours: List[int]):
        self.prior.feedback(word, colours)
        self.guesses_made += 1

    def words_remaining(self) -> int:
        return len(self.vocabulary)

    def best_answer(self) -> Tuple[str, float]:
        return self.prior.best_guess_guess_answer(self.vocabulary)

    def best_entropy(self) -> Tuple[str, float]:
        return self.prior.best_guess_minimise_entropy(self.vocabulary)
