#bigram probabilities
import nltk
from nltk.tokenize import word_tokenize
from nltk import bigrams
from collections import Counter
nltk.download('punkt')
text = "the cat sat on the mat the cat is happy"
tokens = word_tokenize(text.lower())
bigram_list = list(bigrams(tokens))
bigram_counts = Counter(bigram_list)
unigram_counts = Counter(tokens)
bigram_probabilities = {bigram: count / unigram_counts[bigram[0]] for bigram, count in bigram_counts.items()}
print("Bigram Probabilities:")
print(bigram_probabilities)
