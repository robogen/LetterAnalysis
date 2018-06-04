from sys import argv
from re import match
from operator import itemgetter

contents = str("") # Empty string variable to hold file contents
freq = {} # Empty dictionary to hold n-grams of frequency analysis

filename = str(argv[1])
ngram = int(argv[2])

with open(filename, 'r') as con:
    contents = con.read()
	
for analysis in range(0, len(contents), 1):
    temp = str(contents[analysis:analysis+ngram]).lower()
    if not match(r'^[a-zA-Z]{1,11}$', temp) == None: 
        if temp in freq:
            freq[temp] += 1
        else:
            freq[temp] = 1
			
print(sorted(freq.items(), key=itemgetter(1), reverse=True))