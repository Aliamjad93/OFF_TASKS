# Import necessary libraries from TensorFlow and Keras
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from model.Model import file_upload_service

# Class for loading and preparing image datasets
class DataLoader:
    def __init__(self, train_path, test_path, batch_size, image_size):
        # Load training and validation datasets using image_dataset_from_directory
        self.train_ds = keras.utils.image_dataset_from_directory(
            directory=train_path,
            labels='inferred',
            label_mode='binary',
            batch_size=batch_size,
            image_size=image_size
        )
        self.val_ds = keras.utils.image_dataset_from_directory(
            directory=test_path,
            labels='inferred',
            label_mode='binary',
            batch_size=batch_size,
            image_size=image_size
        )

    def process(self, image, label):
        # Preprocess the image data by scaling it to [0, 1]
        image = tf.cast(image / 255., tf.float32)
        return image, label

    def prepare_datasets(self):
        # Apply the preprocessing to the datasets
        self.train_ds = self.train_ds.map(self.process)
        self.val_ds = self.val_ds.map(self.process)

# Class for building and compiling a Keras model
class ModelBuilder:
    def __init__(self):
        self.model = Sequential()

    def build_model(self):
        pass

    def compile_model(self):
        # Compile the model with optimizer and loss function
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def train_model(self, train_ds, val_ds, epochs):
        # Train the model using the training dataset
        self.history = self.model.fit(train_ds, epochs=epochs, validation_data=val_ds)

    def save_model(self, filename):
        # Save the trained model to a file
        self.model.save(filename)

# Class for building a simple Convolutional Neural Network model
class SimpleCNNBuilder(ModelBuilder):
    def build_model(self):
        # Define the architecture of the CNN model
        self.model.add(Conv2D(32, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=(256, 256, 3)))
        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=2, padding='valid'))
        self.model.add(Flatten())
        self.model.add(Dense(1, activation='sigmoid'))

# Class for evaluating and plotting model training results
class ModelEvaluator:
    def __init__(self, history):
        self.history = history

    def plot_results(self):
        # Plot the training and validation accuracy and loss curves
        import matplotlib.pyplot as plt

        plt.plot(self.history.history['accuracy'], color='red', label='train')
        plt.plot(self.history.history['val_accuracy'], color='blue', label='validation')
        plt.plot(self.history.history['loss'], color='red', label='train')
        plt.plot(self.history.history['val_loss'], color='blue', label='validation')
        plt.legend()
        plt.show()

# Main controller class for coordinating data loading, model building, training, and evaluation
class Controller:
    def __init__(self):
        # Initialize data loader, model builder, and evaluator instances
        self.data_loader = DataLoader(
            train_path='C:/Users/farha/.spyder-py3/singleResponsibility/dogs-vs-cats/train',
            test_path='C:/Users/farha/.spyder-py3/singleResponsibility/dogs-vs-cats/test',
            batch_size=32,
            image_size=(256, 256)
        )
        self.model_builder = SimpleCNNBuilder()
        self.model_evaluator = None

    def run(self):
        # Prepare datasets, build, compile, train, and evaluate the model
        self.data_loader.prepare_datasets()
        self.model_builder.build_model()
        self.model_builder.compile_model()
        self.model_builder.train_model(self.data_loader.train_ds, self.data_loader.val_ds, epochs=8)
        self.model_evaluator = ModelEvaluator(self.model_builder.history)
        self.model_evaluator.plot_results()
        self.model_builder.save_model('my_model.h5')

    def predict(self, filename):
        # Call a function from the file_upload_service for prediction
        return file_upload_service.upload_file(filename)

# Create an instance of the Controller class
obj_controller = Controller()

# Uncomment the following line to run the code
# obj_controller.run()
