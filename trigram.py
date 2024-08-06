#trigram
import nltk
from nltk.tokenize import word_tokenize
from nltk import trigrams
from collections import Counter
nltk.download('punkt')
text = "the cat sat on the mat the cat is happy"
tokens = word_tokenize(text.lower())
trigram_list = list(trigrams(tokens))
trigram_counts = Counter(trigram_list)
print("Trigrams:")
print(trigram_counts)
