#python code for unigram model
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')

text = "the cat sat on the mat the cat is happy"

# Tokenize the text
tokens = word_tokenize(text.lower())

# Count unigrams
unigrams = Counter(tokens)

print("Unigrams:")
print(unigrams)
