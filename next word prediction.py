#next word prediction
import nltk
from nltk.tokenize import word_tokenize
from nltk import bigrams
from collections import Counter, defaultdict
nltk.download('punkt')
text = "the cat sat on the mat the cat is happy"

tokens = word_tokenize(text.lower())
bigram_list = list(bigrams(tokens))
bigram_counts = Counter(bigram_list)
unigram_counts = Counter(tokens)
next_word_dict = defaultdict(list)
for (w1, w2), count in bigram_counts.items():
    next_word_dict[w1].append((w2, count / unigram_counts[w1]))

def predict_next_word(word):
    if word in next_word_dict:
    
        next_words = sorted(next_word_dict[word], key=lambda x: x[1], reverse=True)
        return next_words[0][0]
    else:
        return None

print("Next word prediction for 'the':")
print(predict_next_word('the'))
print("Next word prediction for 'cat':")
print(predict_next_word('cat'))
