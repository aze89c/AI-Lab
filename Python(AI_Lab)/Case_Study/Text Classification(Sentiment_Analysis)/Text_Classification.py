import nltk 
from nltk.corpus import movie_reviews 
from nltk import NaiveBayesClassifier 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer 
from nltk import FreqDist 
import random 
 
# Download NLTK resources (uncomment the line below if not downloaded) 
nltk.download('movie_reviews') 
nltk.download('punkt') 
 
def preprocess_text(text): 
    # Tokenize the text 
    words = word_tokenize(text.lower()) 
 
    # Remove stop words 
    stop_words = set(stopwords.words('english')) 
    words = [word for word in words if word.isalpha() and word not in stop_words] 
 
    # Stemming 
    ps = PorterStemmer() 
    words = [ps.stem(word) for word in words] 
 
    return words 
 
def extract_features(words): 
    # Extract features from the words 
    return dict(FreqDist(words)) 
 
def get_dataset(): 
    # Create a dataset for sentiment analysis 
    documents = [(list(movie_reviews.words(fileid)), category) 
                 for category in movie_reviews.categories() 
                 for fileid in movie_reviews.fileids(category)] 
 
    # Shuffle the documents 
    random.shuffle(documents) 
 
    return documents 
 
def train_classifier(dataset): 
    # Train a Naive Bayes classifier 
    featuresets = [(extract_features(words), category) for (words, category) in dataset] 
    return NaiveBayesClassifier.train(featuresets) 
 
def predict_sentiment(classifier, text): 
    # Predict the sentiment of the text 
    words = preprocess_text(text) 
    features = extract_features(words) 
    return classifier.classify(features) 
 
def main(): 
    # Load the movie reviews dataset 
    dataset = get_dataset() 
 
    # Split the dataset into training and testing sets 
    train_set = dataset[:1500] 
    test_set = dataset[1500:] 
 
    # Train the classifier 
    classifier = train_classifier(train_set) 
 
    # Test the classifier on some example reviews 
    example_reviews = [ 
        "I loved this movie! The acting was superb.", 
        "The plot was confusing, and the characters were poorly developed.", 
        "It's an average film with some good and some bad moments.", 
        "This is the worst movie I've ever seen. Terrible acting and a boring plot." 
    ] 
 
    for review in example_reviews: 
        sentiment = predict_sentiment(classifier, review) 
        print(f"Review: {review}\nPredicted Sentiment: {sentiment}\n") 
 
main() 

'''

Output: 
 
Review: I loved this movie! The acting was superb. 
Predicted Sentiment: pos 
 
Review: The plot was confusing, and the characters were poorly developed. 
Predicted Sentiment: neg 
 
Review: It's an average film with some good and some bad moments. 
Predicted Sentiment: neg 
 
Review: This is the worst movie I've ever seen. Terrible acting and a boring plot. 
Predicted Sentiment: neg

'''