from vocabulary import basic, comprehensive
from word_prior import WordPrior

prior = WordPrior.prior(comprehensive)
vocabulary = set(basic())

while True:
    print(
        prior.best_guess_guess_answer(vocabulary),
        prior.best_guess_minimise_entropy(vocabulary),
    )
    try:
        feedback = input("> ")
        word, colours = feedback.split()
        prior.feedback(word, [int(c) for c in colours])
    except Exception:
        continue
