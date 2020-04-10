from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from nltk.corpus import stopwords

def nlp_process(text):
    # Tokenize the string, remove all the punctuations, and make them all lower case
    tokenizer = RegexpTokenizer(r'\w+')
    tokenized_string = tokenizer.tokenize(text)
    tokenized_string = list(map(lambda x: x.lower(), tokenized_string))

    # Count the frequency for words
    fdist1 = FreqDist(tokenized_string)
    common_word = fdist1.most_common(1)
    print(common_word[0])
    #print(f'The word {common_word[0]} appeared {common_word[1]} times in the text')
    print(f'The most common 10 words are: {fdist1.most_common(10)}')

    # Get the association between two words. See: http://www.nltk.org/howto/collocations.html
    bigram_measures = BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(tokenized_string)
    finder.apply_freq_filter(3)
    finder.apply_word_filter(lambda x: x in stopwords.words('english'))
    print(f'The most correlated words are: {finder.nbest(bigram_measures.pmi, 10)}')

    #print(f'\n\n{"#"*20}')
    #print(f'Based on abstract:\n{abstract}')