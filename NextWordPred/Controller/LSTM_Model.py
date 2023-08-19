import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

class Tokenizer:
    def __init__(self):
        text = open("1661-0.txt",encoding="utf-8")
        
        
        lst1 = []
        for i in text:
            lst1.append(i)
            
        data = ""
        for i in lst1:
            data = ' '.join(lst1)
            
        data = data.replace('\n','')
        data = data.replace('\r','')
        data = data.replace('\ufeff','')
        data = data.replace('“','')
        data = data.replace('”','')
        
        
        data = data.split()
        data = ' '.join(data)
        data[:500]
        
        
        from tensorflow.keras.preprocessing.text import Tokenizer
        self.tokenizer = Tokenizer()
        self.tokenizer.fit_on_texts([data])  


Tokenizer=Tokenizer()


# sequence_data = tokenizer.texts_to_sequences([data])[0]
# sequence_data[:15]


# sizeofvocab = len(tokenizer.word_index)+1
# print(sizeofvocab)


# sequences = []

# for i in range(3,len(sequence_data)):
#     words = sequence_data[i-3:i+1]
#     sequences.append(words)
    
# print("Length of sequences: ",len(sequences))
# sequences = np.array(sequences)
# sequences[:10]


# X = []
# y = []

# for i in sequences:
#     X.append(i[0:3])
#     y.append(i[3:5])
    
# X = np.array(X)
# y = np.array(y)


# from tensorflow.keras.utils import to_categorical

# y = to_categorical(y,num_classes=sizeofvocab)


# from tensorflow.keras.layers import Embedding, LSTM, Dense
# from tensorflow.keras.models import Sequential


# model = Sequential()
# model.add(Embedding(sizeofvocab, 10, input_length = 3))
# model.add(LSTM(1000, return_sequences=True))
# model.add(LSTM(1000))
# model.add(Dense(1000,activation='relu'))
# model.add(Dense(sizeofvocab, activation="softmax"))



# model.summary()


# from tensorflow.keras.optimizers import Adam
# model.compile(optimizer=Adam(learning_rate= 0.001), loss="categorical_crossentropy")


# model.fit(X,y,epochs=40,batch_size=64)


# model.save('next_word_prediction.h5')


# from tensorflow.keras.models import load_model

# model = load_model('next_word_prediction.h5')


# # def Predict_next_words(model,tokenizer,text):
    
# #     sequence = tokenizer.texts_to_sequences([text])
# #     sequence = np.array(sequence)
# #     preds = np.argmax(model.predict(sequence))

# #     token = tokenizer.word_index
# #     k1 = [key for key,value in token.items() if value==preds]        
# #     print(k1)
# #     return k1

