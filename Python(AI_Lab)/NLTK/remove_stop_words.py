'''
a) Remove Stop Words 
b) Implementing Stemming 
c) POS (Parts of Speech) tagging 
 
Prerequisites: 
• Install nltk library. 
 
5a) Remove Stop Words '''


# Import libraries 
#import LIbraries 
import nltk 
nltk.download("stopwords") 
from nltk.tokenize import sent_tokenize 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords 
 
# input 
text= """Natural Language Processing with Python provides a practical introduction to programming for 
language processing. Written by the creators of NLTK, it guides the reader through the fundamentals of 
writing Python programs, working with corpora, categorizing text, analyzing linguistic structure, and more. 
The online version of the book has been been updated for Python 3 and NLTK 3.""" 
 
# paragraph to sentence division 
text_to_sentence = sent_tokenize(text) 
print("Paragraph to Sentences") 
print(text_to_sentence) 
print("Number of sentences:",len(text_to_sentence)) 
 
# word division 
tokenized_word = word_tokenize(text) 
print("\nList of Words",tokenized_word) 
print("Number of Words",len(tokenized_word)) 
 
# Stop word removal 
sw_nltk = stopwords.words('english') 
print("\nList of all stop words\n:",sw_nltk) 
print("Number of stop words",len(sw_nltk)) 
words = [word for word in text.split() if word.lower() not in sw_nltk] 
new_text = " ".join(words) 
print(new_text) 
print("\nOld length: ", len(text)) 
print("\nNew length: ", len(new_text)) 
print("\nActual Text\n:",text) 
print("\n Text after removing Stop words:\n",new_text) 
 

 
 
'''
 
Output: 
 
Paragraph to Sentences 
['Natural Language Processing with Python provides a practical introduction to programming for language 
processing.', 'Written by the creators of NLTK, it guides the reader through the fundamentals of writing Python 
programs, working with corpora, categorizing text, analyzing linguistic structure, and more.', 'The online version 
of the book has been been updated for Python 3 and NLTK 3.'] 
Number of sentences: 3 
 
List of Words ['Natural', 'Language', 'Processing', 'with', 'Python', 'provides', 'a', 'practical', 'introduction', 'to', 
'programming', 'for', 'language', 'processing', '.', 'Written', 'by', 'the', 'creators', 'of', 'NLTK', ',', 'it', 'guides', 
'the', 'reader', 'through', 'the', 'fundamentals', 'of', 'writing', 'Python', 'programs', ',', 'working', 'with', 'corpora', 
',', 'categorizing', 'text', ',', 'analyzing', 'linguistic', 'structure', ',', 'and', 'more', '.', 'The', 'online', 'version', 'of', 
'the', 'book', 'has', 'been', 'been', 'updated', 'for', 'Python', '3', 'and', 'NLTK', '3', '.'] 
Number of Words 65 
 
List of all stop words 
: ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 
'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 
'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 
'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 
'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 
'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 
'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 
'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', 
"should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', 
"doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', 
"mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', 
"won't", 'wouldn', "wouldn't"] 
Number of stop words 179 
Natural Language Processing Python provides practical introduction programming language processing. Written 
creators NLTK, guides reader fundamentals writing Python programs, working corpora, categorizing text, 
analyzing linguistic structure, more. online version book updated Python 3 NLTK 3. 
 
Old length: 381 
New length: 293 
Actual Text 
: Natural Language Processing with Python provides a practical introduction to programming for language 
processing. Written by the creators of NLTK, it guides the reader through the fundamentals of writing Python 
programs, working with corpora, categorizing text, analyzing linguistic structure, and more. The online version 
of the book has been been updated for Python 3 and NLTK 3. 
 
Text after removing Stop words: 
Natural Language Processing Python provides practical introduction programming language processing. 
Written creators NLTK, guides reader fundamentals writing Python programs, working corpora, categorizing 
text, analyzing linguistic structure, more. online version book updated Python 3 NLTK 3.

'''