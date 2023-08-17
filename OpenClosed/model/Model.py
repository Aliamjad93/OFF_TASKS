# Importing necessary libraries
from fastapi import UploadFile  # Importing UploadFile from FastAPI for file uploads
from tensorflow import keras  # Importing Keras from TensorFlow
from fastapi.responses import JSONResponse  # Importing JSONResponse from FastAPI for sending JSON responses
from abc import ABC, abstractmethod  # Importing ABC (Abstract Base Class) for abstract classes
import cv2  # Importing OpenCV for image processing
import os  # Importing the os module for file operations

# Abstract class for ImageClassifier
class ImageClassifier(ABC):
    @abstractmethod
    def predict(self, test_input):
        pass

# Concrete class for CatDogImageClassifier that implements ImageClassifier
class CatDogImageClassifier(ImageClassifier):
    def __init__(self):
        # Load the trained model when an instance is created
        self.loaded_model = keras.models.load_model(r"C:\Users\farha\.spyder-py3\singleResponsibility\my_model.h5")

    def predict(self, test_input):
        # Perform prediction using the loaded model
        if self.loaded_model.predict(test_input) > 0.5:
            return JSONResponse(content={"message": "The Object in image is -- DOG"})
        else:
            return JSONResponse(content={"message": "The Object in image is -- CAT"})

# Service class for uploading files and making predictions
class FileUploadService:
    def __init__(self, image_classifier: ImageClassifier):
        self.image_classifier = image_classifier

    def upload_file(self, file: UploadFile):
        upload_dir = "uploaded_images"
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        img = cv2.imread(rf'{file_path}')
        test_img = cv2.resize(img, (256, 256))
        test_input = test_img.reshape((1, 256, 256, 3))

        result = self.image_classifier.predict(test_input)
        return result

# Creating an instance of CatDogImageClassifier
cat_dog_classifier = CatDogImageClassifier()

# Creating an instance of FileUploadService with the image classifier instance
file_upload_service = FileUploadService(cat_dog_classifier)
