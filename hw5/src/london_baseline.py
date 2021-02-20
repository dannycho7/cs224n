# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import os
from utils import evaluate_places

dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, '../birth_dev.tsv')

num_examples = sum(1 for line in open(filepath))
total, correct = evaluate_places(filepath, ["London" for _ in range(num_examples)])
print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))