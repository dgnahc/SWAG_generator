# Install NLTK - pip install nltk

import nltk
#nltk.download()

paragraph = "Thanks you all Night. But I am sad."


print(nltk.sent_tokenize(paragraph)) # return all the separate sentences

print(nltk.word_tokenize(paragraph)) # return all the separate words


# stemming: may not have a meaning
# sentence 1 John does his work intelligently
# sentence 2 John is an intelligent man
# sentence 3

#Lemmatization
#Word respresentations have meaning
#Takes more time
#use when meaning of words is important for analysis
