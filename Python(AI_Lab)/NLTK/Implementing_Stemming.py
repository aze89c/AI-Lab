#importing the Stemming function from nltk library 
from nltk.stem.porter import PorterStemmer 
#defining a function for stemming 
 
from nltk.stem import PorterStemmer 
from nltk.stem import SnowballStemmer 
snowball = SnowballStemmer(language='english') 
 
#defining the object for stemming 
text= """Natural Language Processing with Python provides a practical introduction to programming for 
language processing. Written by the creators of NLTK, it guides the reader through the fundamentals of 
writing Python programs, working with corpora, categorizing text, analyzing linguistic structure, and more. 
The online version of the book has been been updated for Python 3 and NLTK 3.""" 
 
stemmer = PorterStemmer() 
def stem_words(text): 
    return " ".join([stemmer.stem(word) for word in text.split()]) 
stemmed_data=stem_words(text) 
print("Actual text\n",text) 
print("stemmed text\n:" ,stemmed_data) 
        
 
'''
Output: 
 
 
Actual text 
Natural Language Processing with Python provides a practical introduction to programming for language 
processing. Written by the creators of NLTK, it guides the reader through the fundamentals of writing Python 
programs, working with corpora, categorizing text, analyzing linguistic structure, and more. The online version 
of the book has been been updated for Python 3 and NLTK 3. 
 
stemmed text 
: natur languag process with python provid a practic introduct to program for languag processing. written by 
the creator of nltk, it guid the reader through the fundament of write python programs, work with corpora, 
categor text, analyz linguist structure, and more. the onlin version of the book ha been been updat for python 3 
and nltk 3. 
 
 '''
 
 
 
 
 
 
