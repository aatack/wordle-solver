from typing import List

from letter_prior import LetterPrior


class WordPrior:
    def __init__(self, letter_priors: List[LetterPrior]):
        self._letter_priors = letter_priors
