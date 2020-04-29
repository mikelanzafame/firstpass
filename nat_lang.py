from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from nltk.corpus import stopwords

def nlp_process(text):
    # Tokenize the string, remove all the punctuations, and make them all lower case
    tokenizer = RegexpTokenizer(r'\w+')
    tokenized_string = tokenizer.tokenize(text)
    tokenized_string = list(map(lambda x: x.lower(), tokenized_string))
    stop_words = set(stopwords.words('english')) 

    # Stopword Removal
    stop_removed = []
    for word in tokenized_string:
        if word not in stop_words:
            stop_removed.append(word)

    # Count the frequency for words
    fdist1 = FreqDist(stop_removed)
    common_word = fdist1.most_common(1)
    top_word, top_freq = common_word[0]
    print("the most common word '{top_word}' occours {top_freq} times in the sampled text.".format(top_word = top_word, top_freq = top_freq))
    print(f'The most common 10 words are: {fdist1.most_common(10)}')

    # Get the association between two words. See: http://www.nltk.org/howto/collocations.html
    bigram_measures = BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(stop_removed)
    finder.apply_freq_filter(3)
    finder.apply_word_filter(lambda x: x in stopwords.words('english'))
    print(f'The most correlated words are: {finder.nbest(bigram_measures.pmi, 10)}')
