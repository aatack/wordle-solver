from solver import Solver

solver = Solver()

current_guess = 0
while True:
    print("\n" * 5)
    print("Current guess:", current_guess)
    print(solver.best_answer(), solver.best_entropy())

    feedback = input("> ")
    word, colours = feedback.split()
    solver.guess(word, [int(c) for c in colours])

    # vocabulary.prune(prior)
    print(f"Words remaining: {solver.words_remaining()}")

    print(f"Current prior: (entropy = {solver.prior.total_entropy})")
    print(solver.prior)
    print()
