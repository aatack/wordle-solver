from vocabulary import Vocabulary, basic, comprehensive
from word_prior import WordPrior

# prior = WordPrior.prior(basic)
prior = WordPrior.uniform()
vocabulary = Vocabulary(set(basic()))

while True:
    print(
        prior.best_guess_guess_answer(vocabulary),
        prior.best_guess_minimise_entropy(vocabulary),
    )

    feedback = input("> ")
    word, colours = feedback.split()
    prior.feedback(word, [int(c) for c in colours])

    vocabulary.prune(prior)
    print(f"Words remaining: {len(vocabulary)}")

    print("Current prior:")
    print(prior)
    print()

