# create a dictionary with words counts in corpus
from collections import Counter
f = open("/Users/jacqueline/Desktop/Catalina Corpus.txt")
text1 = f.read()
words = [word.lower() for word in text1.split()]
word_freq = Counter(words)

for item in word_freq.most_common(50):
    print("{}:{}".format(*item))

stop_words = [x.strip("\n") for x in
open("/Users/jacqueline/nltk_data/corpora/stopwords/spanish").readlines()]

for word in stop_words:
    del word_freq[word]

for item in word_freq.most_common(100):
    print("{}:{}".format(*item))

with open("/Users/jacqueline/Desktop/All_Word_Couts.txt", "w") as output:
    for item in word_freq.most_common():
        output.write(("{}:{}\n".format(*item)))

