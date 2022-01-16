class Colours:
    BLACK = 0
    YELLOW = 1
    GREEN = 2


ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Somewhat arbitrary factor that corresponds to the amount by which we boost the prior
# probability of a letter in position i when that letter in position j led to yellow
# feedback.  Higher values lead to a greater increase in probability
INFERENCE_FACTOR = 1.01

INITIAL_OFFSET = 0.0
