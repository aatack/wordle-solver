from vocabulary import Vocabulary, comprehensive
from word_prior import WordPrior

# TODO: turn this into a hyperparameter
to_use = comprehensive

prior = WordPrior.uniform()
vocabulary = Vocabulary(set(to_use()))

current_guess = 0
while True:
    current_guess += 1

    print("\n" * 5)
    print("Current guess:", current_guess)
    print(
        prior.best_guess_guess_answer(vocabulary),
        prior.best_guess_minimise_entropy(vocabulary),
    )

    feedback = input("> ")
    word, colours = feedback.split()
    prior.feedback(word, [int(c) for c in colours])

    # vocabulary.prune(prior)
    print(f"Words remaining: {len(vocabulary)}")

    print(f"Current prior: (entropy = {prior.total_entropy})")
    print(prior)
    print()
