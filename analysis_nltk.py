from nltk import word_tokenize, Text
from nltk.probability import FreqDist

tokens = ""

with open(u'monte_cristo.txt', 'r', encoding="utf8") as con:
    contents = con.read()
    tokens = word_tokenize(contents)
	
processed = Text(tokens)
fdist = FreqDist(processed)
processed.collocations()
print(fdist.most_common(50))
fdist.plot(50)