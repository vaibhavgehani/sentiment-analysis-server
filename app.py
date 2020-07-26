from flask import Flask,request,jsonify
from flask_cors import CORS
import pickle
app=Flask(__name__)
CORS(app)
from ocr_text import ocr_core

classifier=pickle.load(open('classifier.pkl','rb'))

def extract_features(word_list):
    return dict([(word, True) for word in word_list])

def predictSentiment(text):
    print('predict Sentiement',text)
    probdist = classifier.prob_classify(extract_features(text.split()))
    pred_sentiment = probdist.max()
    print("Predicted sentiment: ", pred_sentiment)
    return pred_sentiment
    
@app.route('/')
def index():
    return "Hello"

@app.route('/getText',methods=['POST'])
def getText():
    file=request.files['file']
    text = ocr_core(file)
    # print(type(text))
    sentiment = predictSentiment(text)
    print(sentiment)
    return jsonify(outputText=text,predSentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)