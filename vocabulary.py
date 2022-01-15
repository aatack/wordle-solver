from typing import Iterator


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
