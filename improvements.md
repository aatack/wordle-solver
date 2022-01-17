-   See TODOs around the folder.
-   Hyperparameter sweep.
-   Only allow final guesses from the simplified list.
-   Consider using p > n / (n + 1) for the guess criterion.
    Or the probability of the most likely word must be > 0.5 _or_ more than twenty times the probability of the previous highest-probability word (on the last turn it would have been guessed).
-   Catch exceptions when typing.
-   Do not display zero-probability letters, and show them in descending order.
-   Once 5 letters have been seen, set probability of the remaining letters to zero.
-   Note that greens and yellows *do* stack, but yellows and blacks *do not*.
    Eg. guessing `taata` for `abate` gives `01221` raw feedback.
-   Guess from the basic list, unless there are none left; then fall back to the comprehensive list.