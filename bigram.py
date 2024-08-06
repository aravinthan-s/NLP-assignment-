#bigram
import nltk
from nltk.tokenize import word_tokenize
from nltk import bigrams
from collections import Counter
nltk.download('punkt')
text = "the cat sat on the mat the cat is happy"
tokens = word_tokenize(text.lower())
bigram_list = list(bigrams(tokens))
bigram_counts = Counter(bigram_list)

print("Bigrams:")
print(bigram_counts)
