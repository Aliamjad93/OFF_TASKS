from keras.models import load_model
import nltk
nltk.download('punkt')#Sentence tokenizer

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import warnings
import numpy as np
import random
warnings.filterwarnings('ignore')

class Controller:
    
    def __init__(self):
        with open(r'C:\Users\farha\.spyder-py3\Task1\ChatBot\Controller\config.json') as config_file:
            config = json.load(config_file)
        
        self.model = load_model(config['model'])
        self.intents = json.loads(open(config['intents']).read())
        self.words = pickle.load(open(config['words'], 'rb'))
        self.classes = pickle.load(open(config['classes'], 'rb'))
        
        #Utility Methods

    def clean_up_sentence(self,sentence): # tokenize the pattern - split words into array
    
        sentence_words = nltk.word_tokenize(sentence)
        # stem each word - create short form for word
    
        sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        #print(sentence_words)
    
        return sentence_words
        #return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
    
    def bow(self,sentence, words, show_details=True): # tokenize the pattern
    
        sentence_words = self.clean_up_sentence(sentence)
    
        # bag of words - matrix of N words, vocabulary matrix
    
        bag = [0]*len(self.words) 
        #print(bag)
    
        for s in sentence_words:  
            for i,w in enumerate(self.words):
                
                if w == s: 
                    # assign 1 if current word is in the vocabulary position
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)

        return(np.array(bag))
    
    def predict_class(self,sentence, model): # filter out predictions below a threshold
    
        p = self.bow(sentence, self.words,show_details=False)
        
    
        res = self.model.predict(np.array([p]))[0]
        
    
        ERROR_THRESHOLD = 0.25
    
        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]

    
        results.sort(key=lambda x: x[1], reverse=True)
    
        return_list = []
    
        for r in results:
            return_list.append({"intent":self.classes[r[0]], "probability": str(r[1])})
    
        return return_list
    
    def getResponse(self,ints, intents_json):

        tag = ints[0]['intent']
    
        list_of_intents = intents_json['intents']
    
        for i in list_of_intents:
            if(i['tag']== tag):
                result = random.choice(i['responses'])
                break
        return result
    
    def chatbot_response(self,text): 
         ints = self.predict_class(text, self.model) 
         res = self.getResponse(ints, self.intents)
        
         return res


    def AskQuestion(self,query):
          try:
              res = self.chatbot_response(query)
              return res
          except:
              return ('You may need to rephrase your question.')
              
              
controller=Controller()
        
    
    
    