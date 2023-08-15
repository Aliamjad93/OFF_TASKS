import tensorflow as tf
from tensorflow import keras
from keras import Sequential
import matplotlib.pyplot as plt
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten
from model.Model import fileupload


from fastapi import UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os


class Controller:
    
    # defining init method to declared train_ds and val_ds because these attrs used in whole class
    def __init__(self):
        
    
    
    #defining Traintest function to get images from train and test directory and set batch size 32
    # and make each image size is 256,256. because images is in different sizes
    
        self.train_ds=keras.utils.image_dataset_from_directory(directory='C:/Users/farha/.spyder-py3/catVsdog/dogs-vs-cats/train',
                                                  labels='inferred',
                                                  label_mode='int',
                                                  batch_size=32,
                                                  image_size=(256,256))

        self.val_ds=keras.utils.image_dataset_from_directory(directory='C:/Users/farha/.spyder-py3/catVsdog/dogs-vs-cats/test',
                                                  labels='inferred',
                                                  label_mode='int',
                                                  batch_size=32,
                                                  image_size=(256,256))
        
    
    #Normalize Data
    def process(self,image,label):
        image=tf.cast(image/255. , tf.float32)
        return image,label
    
    def train_valDS(self):


        self.train_ds=self.train_ds.map(self.process)
        self.val_ds=self.val_ds.map(self.process)
        
        
        #Create CNN Model
    def CreatingModel(self):
        
        self.model=Sequential()
        self.model.add(Conv2D(32, kernel_size=(3,3),padding='valid',activation='relu',input_shape=(256,256,3)))
        self.model.add(MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'))



        self.model.add(Conv2D(64, kernel_size=(3,3),padding='valid',activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'))



        self.model.add(Conv2D(128, kernel_size=(3,3),padding='valid',activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'))

        self.model.add(Flatten())

        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))



        self.model.summary()


        # #evaluation

        self.model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
    
        # # #training
    def TrainModel(self):
        


        self.history=self.model.fit(self.train_ds,epochs=8,validation_data=self.val_ds)
        
     
      # plot the results of training, like accuracy and validation score   
     
    def Plotting(self):
        
        plt.plot(self.history.history['accuracy'],color='red',label='train')
        plt.plot(self.history.history['val_accuracy'],color='blue',label='validation')




        plt.plot(self.history.history['loss'],color='red',label='train')
        plt.plot(self.history.history['val_loss'],color='blue',label='validation')
        
    def SaveModel(self):
        self.model.save('my_model.h5')
        
        
        

    def predict(self,filename):
        
        
        # fileupload.upload_file(filename)
        return fileupload.upload_file(filename)
        
        
       
    
    
        
        





        
obj_contoller=Controller()

# obj_contoller.train_valDS()
# obj_contoller.CreatingModel()
# obj_contoller.TrainModel()




































