import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import pickle
positive_fileids = movie_reviews.fileids('pos')
negative_fileids = movie_reviews.fileids('neg')


def extract_features(word_list):
    return dict([(word, True) for word in word_list])

features_positive = [(extract_features(movie_reviews.words(fileids=[f])),'Positive') for f in positive_fileids]
features_negative = [(extract_features(movie_reviews.words(fileids=[f])),'Negative') for f in negative_fileids]

threshold_factor = 0.8
threshold_positive = int(threshold_factor * len(features_positive))
threshold_negative = int(threshold_factor * len(features_negative))

features_train = features_positive[:threshold_positive]+features_negative[:threshold_negative]
features_test = features_positive[threshold_positive:]+features_negative[threshold_negative:]

classifier = NaiveBayesClassifier.train(features_train)
pickle.dump(classifier,open('classifier.pkl','wb'))

# probdist = classifier.prob_classify(extract_features("You are bad".split()))
# pred_sentiment = probdist.max()
# print("Predicted sentiment: ", pred_sentiment)