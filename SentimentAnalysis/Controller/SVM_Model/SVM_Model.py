import re
from nltk.corpus import stopwords
import pandas as pd
import time
from sklearn import svm
from sklearn.metrics import classification_report

import nltk
import re
import joblib
from nltk.corpus import stopwords
nltk.download('stopwords')

col_names = ['ID', 'Entity', 'Sentiment', 'Content']
df=pd.read_csv(r'C:\Users\farha\.spyder-py3\Task1\SentimentAnalysis\Controller\SVM_Model\twitter_training.csv',names=col_names)
test_df=pd.read_csv(r'C:\Users\farha\.spyder-py3\Task1\SentimentAnalysis\Controller\SVM_Model\twitter_validation.csv',names=col_names)

dfq= df.drop(["Entity","ID"],axis=1)



def clean_text(text):
    # Remove numbers
    text = re.sub(r'\d+', '', str(text))

    # Remove special characters
    text = re.sub(r'[^\w\s]', '', str(text))

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = text.lower().split()
    text = ' '.join([word for word in tokens if word not in stop_words])

    return text

dfq['Cleaned_text']=dfq['Content'].apply(clean_text)

Quality_df=dfq.drop('Content', axis=1)

Quality_df['word_count'] = Quality_df['Cleaned_text'].apply(lambda x: len(x.split()))

Q_dataset=Quality_df.drop(['word_count'], axis=1)

test_df.drop(columns=['ID','Entity'],inplace=True)

test_df["Cleaned_text"]=test_df["Content"].apply(clean_text)

test=test_df.drop("Content", axis=1)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(min_df = 5,
                             max_df = 0.8,
                             sublinear_tf = True,
                             use_idf = True)
train_vectors = vectorizer.fit_transform(Q_dataset['Cleaned_text'])
test_vectors = vectorizer.transform(test['Cleaned_text'])



# classifier_linear = svm.SVC(kernel='linear')
# t0 = time.time()
# classifier_linear.fit(train_vectors, Q_dataset['Sentiment'])
# t1 = time.time()
# prediction_linear = classifier_linear.predict(test_vectors)
# t2 = time.time()
# time_linear_train = t1-t0
# time_linear_predict = t2-t1

# print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
# report = classification_report(test['Sentiment'], prediction_linear, output_dict=True)
# print('positive: ', report['Positive'])
# print('negative: ', report['Negative'])
# print('neutral: ', report['Neutral'])


# model_filename = 'svm_model.pkl'
# joblib.dump(classifier_linear, model_filename)




