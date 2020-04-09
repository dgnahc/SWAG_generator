import nltk

#nltk.download('maxent_ne_chunker')
#nltk.download('words')

#This program categorize the word phrase into "Person", "Organization", etc.


paragraph = "The Taj Mahal was built by Emperor Shah Jahan"

words = nltk.word_tokenize(paragraph)

tagged_words = nltk.pos_tag(words)

namedEnt = nltk.ne_chunk(tagged_words)

namedEnt.draw()
