import tensorflow as tf
from tensorflow import keras
from keras import Sequential
import matplotlib.pyplot as plt
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from model.Model import file_upload_service 
class DataLoader:
    def __init__(self, train_path, test_path, batch_size, image_size):
        self.train_ds = keras.utils.image_dataset_from_directory(
            directory=train_path,
            labels='inferred',
            label_mode='int',
            batch_size=batch_size,
            image_size=image_size
        )
        self.val_ds = keras.utils.image_dataset_from_directory(
            directory=test_path,
            labels='inferred',
            label_mode='int',
            batch_size=batch_size,
            image_size=image_size
        )

    def process(self, image, label):
        image = tf.cast(image / 255., tf.float32)
        return image, label

    def prepare_datasets(self):
        self.train_ds = self.train_ds.map(self.process)
        self.val_ds = self.val_ds.map(self.process)

class ModelBuilder:
    def __init__(self):
        self.model = Sequential()

    def build_model(self):
        pass  # To be implemented by concrete model builders

    def compile_model(self):
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def train_model(self, train_ds, val_ds, epochs):
        self.history = self.model.fit(train_ds, epochs=epochs, validation_data=val_ds)

    def save_model(self, filename):
        self.model.save(filename)

class SimpleCNNBuilder(ModelBuilder):
    def build_model(self):
        self.model.add(Conv2D(32, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=(256, 256, 3)))
        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=2, padding='valid'))

        # ... add more layers ...

        self.model.add(Dense(1, activation='sigmoid'))

class ComplexCNNBuilder(ModelBuilder):
    def build_model(self):
        self.model.add(Conv2D(64, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=(256, 256, 3)))
        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=2, padding='valid'))

        # ... add more complex layers ...

        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))

class ModelEvaluator:
    def __init__(self, history):
        self.history = history

    def plot_results(self):
        plt.plot(self.history.history['accuracy'], color='red', label='train')
        plt.plot(self.history.history['val_accuracy'], color='blue', label='validation')

        plt.plot(self.history.history['loss'], color='red', label='train')
        plt.plot(self.history.history['val_loss'], color='blue', label='validation')
        plt.legend()
        plt.show()

class Controller:
    def __init__(self, model_builder):
        self.data_loader = DataLoader(
            train_path='C:/Users/farha/.spyder-py3/singleResponsibility/dogs-vs-cats/train',
            test_path='C:/Users/farha/.spyder-py3/singleResponsibility/dogs-vs-cats/test',
            batch_size=32,
            image_size=(256, 256)
        )
        self.model_builder = model_builder()
        self.model_evaluator = None

    def run(self):
        self.data_loader.prepare_datasets()
        self.model_builder.build_model()
        self.model_builder.compile_model()
        self.model_builder.train_model(self.data_loader.train_ds, self.data_loader.val_ds, epochs=8)
        self.model_evaluator = ModelEvaluator(self.model_builder.history)
        self.model_evaluator.plot_results()
        self.model_builder.save_model('my_model.h5')
        
    def predict(self,filename):
        return file_upload_service.upload_file(filename)
        



obj_controller = Controller(model_builder=SimpleCNNBuilder)
# obj_controller.run()



















































