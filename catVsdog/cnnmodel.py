import tensorflow as tf
from tensorflow import keras
from keras import Sequential
import matplotlib.pyplot as plt
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten     #importing required modules
from model.Model import fileupload


from fastapi import UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os


class MakeCNNModel:
    
    # defining init method to declared train_ds and val_ds because these attrs used in whole class
    def __init__(self):
        
    
    
    #defining Traintest function to get images from train and test directory and set batch size 32
    # and make each image size is 256,256. because images is in different sizes
    
    
   
    
        self.train_ds=keras.utils.image_dataset_from_directory(directory='C:/Users/farha/.spyder-py3/Task1/catVsdog/dogs-vs-cats/train',
                                                  labels='inferred',
                                                  label_mode='int',
                                                  batch_size=32,
                                                  image_size=(256,256))

        self.val_ds=keras.utils.image_dataset_from_directory(directory='C:/Users/farha/.spyder-py3/Task1/catVsdog/dogs-vs-cats/test',
                                                  labels='inferred',
                                                  label_mode='int',
                                                  batch_size=32,
                                                  image_size=(256,256))
        
    
    #Normalize Data
    def process(self, image, label):
        # Convert pixel values to floating-point in the range [0, 1]
        image = tf.cast(image / 255., tf.float32)
        
        # Return the preprocessed image and its associated label
        return image, label

    
    def train_valDS(self):


        self.train_ds=self.train_ds.map(self.process)
        self.val_ds=self.val_ds.map(self.process)
        
        
        #Create CNN Model
    def CreatingModel(self):
                
                # Creating a Sequential model for building the neural network
        self.model = Sequential()
        
        # Adding a convolutional layer with 32 filters, each of size (3,3)
        # Activation function used is ReLU (Rectified Linear Unit)
        # Input shape for the first layer is (256, 256, 3) representing an image with dimensions 256x256 and 3 color channels (RGB)
        self.model.add(Conv2D(32, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=(256, 256, 3)))
        
        # Adding a MaxPooling layer to perform downsampling
        # Pooling size is (2,2), which reduces the spatial dimensions by a factor of 2
        # Valid padding is used, which means no padding is added to the input before pooling
        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=2, padding='valid'))
        
        # Adding another convolutional layer with 64 filters, activation function is ReLU
        self.model.add(Conv2D(64, kernel_size=(3, 3), padding='valid', activation='relu'))
        
        # Adding another MaxPooling layer after the second convolutional layer
        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=2, padding='valid'))
        
        # Adding one more convolutional layer with 128 filters, activation function is ReLU
        self.model.add(Conv2D(128, kernel_size=(3, 3), padding='valid', activation='relu'))
        
        # Adding another MaxPooling layer after the third convolutional layer
        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=2, padding='valid'))
        
        # Flattening the output from the convolutional layers to prepare for fully connected layers
        self.model.add(Flatten())
        
        # Adding a fully connected layer with 128 units, activation function is ReLU
        self.model.add(Dense(128, activation='relu'))
        
        # Adding another fully connected layer with 64 units, activation function is ReLU
        self.model.add(Dense(64, activation='relu'))
        
        # Adding the output layer with a single unit and sigmoid activation function
        # This is a binary classification problem, so sigmoid activation is used to get a probability value
        self.model.add(Dense(1, activation='sigmoid'))
        
        # Printing a summary of the model architecture, showing the layer types, output shapes, and number of parameters
        self.model.summary()
        
        # Compiling the model using the Adam optimizer and binary cross-entropy loss
        # The metric to track during training is accuracy
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        # This code creates a convolutional neural network
            
        # # #training
    def TrainModel(self):
        


        self.history=self.model.fit(self.train_ds,epochs=8,validation_data=self.val_ds)
        
     
      # plot the results of training, like accuracy and validation score   
     
    def Plotting(self):
        
        plt.plot(self.history.history['accuracy'],color='red',label='train')
        plt.plot(self.history.history['val_accuracy'],color='blue',label='validation')




        plt.plot(self.history.history['loss'],color='red',label='train')
        plt.plot(self.history.history['val_loss'],color='blue',label='validation')
        
    
    #saving my model 
    def SaveModel(self):
        self.model.save('my_model.h5')
