#5c. POS (Parts of Speech) tagging 
 
#import Libraries 
#import Libraries 
import nltk 
nltk.download('averaged_perceptron_tagger') 
text= """Natural Language Processing with Python provides a practical introduction to programming for 
language processing. Written by the creators of NLTK, it guides the reader through the fundamentals of 
writing Python programs, working with corpora, categorizing text, analyzing linguistic structure, and more. 
The online version of the book has been been updated for Python 3 and NLTK 3.""" 
 
tokens = nltk.word_tokenize(text) 
print(tokens) 
 
tag = nltk.pos_tag(tokens)
print(tag) 

 
 
 
 
'''

Output: 
['Natural', 'Language', 'Processing', 'with', 'Python', 'provides', 'a', 'practical', 'introduction', 'to', 
'programming', 'for', 'language', 'processing', '.', 'Written', 'by', 'the', 'creators', 'of', 'NLTK', ',', 
'it', 'guides', 'the', 'reader', 'through', 
'the', 'fundamentals', 'of', 'writing', 'Python', 'programs', ',', 'working', 'with', 'corpora', ',', 
'categorizing', 'text', ',', 
'analyzing', 'linguistic', 'structure', ',', 'and', 'more', '.', 'The', 'online', 'version', 'of', 'the', 
'book', 'has', 'been', 'been', 'updated', 'for', 'Python', '3', 'and', 'NLTK', '3', '.'] 
 
[('Natural', 'JJ'), ('Language', 'NNP'), ('Processing', 'NNP'), ('with', 'IN'), ('Python', 'NNP'), 
('provides', 'VBZ'), 
('a', 'DT'), ('practical', 'JJ'), ('introduction', 'NN'), ('to', 'TO'), ('programming', 'VBG'), ('for', 
'IN'), ('language', 
'NN'), ('processing', 'NN'), ('.', '.'), ('Written', 'VBN'), ('by', 'IN'), ('the', 'DT'), ('creators', 
'NNS'), ('of', 'IN'), 
('NLTK', 'NNP'), (',', ','), ('it', 'PRP'), ('guides', 'VBZ'), ('the', 'DT'), ('reader', 'NN'), ('through', 
'IN'), ('the', 'DT'), 
('fundamentals', 'NNS'), ('of', 'IN'), ('writing', 'VBG'), ('Python', 'NNP'), ('programs', 'NNS'), 
(',', ','), ('working', 
'VBG'), ('with', 'IN'), ('corpora', 'NNS'), (',', ','), ('categorizing', 'VBG'), ('text', 'NN'), (',', ','), 
('analyzing', 'VBG'), 
('linguistic', 'JJ'), ('structure', 'NN'), (',', ','), ('and', 'CC'), ('more', 'RBR'), ('.', '.'), ('The', 'DT'), 
('online', 'JJ'), 
('version', 'NN'), ('of', 'IN'), ('the', 'DT'), ('book', 'NN'), ('has', 'VBZ'), ('been', 'VBN'), ('been', 
'VBN'), ('updated', 
'VBN'), ('for', 'IN'), ('Python', 'NNP'), ('3', 'CD'), ('and', 'CC'), ('NLTK', 'NNP'), ('3', 'CD'), 
('.', '.')] 
 
'''
 
 
 
