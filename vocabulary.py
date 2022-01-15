from random import choice, choices, uniform
from typing import Iterator, List, Set

from word_prior import WordPrior


def basic() -> Iterator[str]:
    with open("data/basic.txt") as file:
        for word in file.readlines():
            assert len(word.strip()) == 5, f"'{word}'"
            yield word.strip()


def comprehensive() -> Iterator[str]:
    with open("data/comprehensive.txt") as file:
        for line in file.readlines():
            for word in line.split():
                if len(word) == 0:
                    continue
                assert len(word) == 5
                yield word.lower()


class Vocabulary:
    def __init__(self, words: Set[str]):
        self._words = words

    def __len__(self) -> int:
        return len(self._words)

    def prune(self, prior: WordPrior):
        for word in set(self._words):
            if prior[word] < 1e-8:
                self._words.remove(word)

    def sample(self, count: int, prior: WordPrior) -> str:
        words = list(self._words)
        return choices(words, weights=[prior[word] for word in words], k=count)

    def uniform_sample(self, count: int) -> List[str]:
        return choices(list(self._words), k=count)

    def all_words(self) -> List[str]:
        return list(self._words)
