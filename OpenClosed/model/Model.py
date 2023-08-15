from fastapi import UploadFile
from tensorflow import keras
from fastapi.responses import JSONResponse
from abc import ABC, abstractmethod
import cv2
import os

class ImageClassifier(ABC):
    @abstractmethod
    def predict(self, test_input):
        pass

class CatDogImageClassifier(ImageClassifier):
    def __init__(self):
        self.loaded_model = keras.models.load_model(r"C:\Users\farha\.spyder-py3\singleResponsibility\my_model.h5")

    def predict(self, test_input):
        if self.loaded_model.predict(test_input) > 0.5:
            return JSONResponse(content={"message": "The Object in image is -- DOG"})
        else:
            return JSONResponse(content={"message": "The Object in image is -- CAT"})

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

# Usage
cat_dog_classifier = CatDogImageClassifier()
file_upload_service = FileUploadService(cat_dog_classifier)
