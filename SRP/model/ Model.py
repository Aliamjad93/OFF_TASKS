# Import necessary libraries from FastAPI
from fastapi import UploadFile, File, HTTPException
from tensorflow import keras
from fastapi.responses import JSONResponse
import cv2
import os

# Class for predicting objects in images using a pre-trained model
class ModelPredictor:
    
    def __init__(self, model_path):
        # Load the pre-trained model from the given path
        self.loaded_model = keras.models.load_model(model_path)
        
    def predictPic(self, file_path):
        # Read and preprocess the image using OpenCV
        img = cv2.imread(rf'{file_path}')
        test_img = cv2.resize(img, (256, 256))
        test_input = test_img.reshape((1, 256, 256, 3))
        
        # Perform prediction using the loaded model
        if self.loaded_model.predict(test_input) > 0.5:
            # If the prediction score is above 0.5, classify as "DOG"
            return "DOG"
        else:
            # Otherwise, classify as "CAT"
            return "CAT"

# Class for uploading images
class ImageUploader:
    def __init__(self):
        self.upload_dir = "uploaded imagess"
        
        # Create the upload directory if it doesn't exist
        os.makedirs(self.upload_dir, exist_ok=True)

    def upload(self, file):
        # Save the uploaded file to the upload directory
        file_path = os.path.join(self.upload_dir, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return file_path

# Class for handling file uploads and predicting object in the image
class FileUploadService:
    def __init__(self, model_path):
        # Initialize the ModelPredictor and ImageUploader instances
        self.model_predictor = ModelPredictor(model_path)
        self.image_uploader = ImageUploader()

    def upload_file(self, file: UploadFile = File(...)):
        # Upload the file and get the file path
        file_path = self.image_uploader.upload(file)
        
        # Perform prediction using the ModelPredictor
        prediction = self.model_predictor.predictPic(file_path)

        # Return a JSON response indicating the predicted object
        return JSONResponse(content={"message": f"The Object in the image is: {prediction}"})


# Example usage

# Define the path to the pre-trained model
model_path = r"C:\Users\farha\.spyder-py3\singleResponsibility\my_model.h5"
    
# Create an instance of the FileUploadService
file_upload_service = FileUploadService(model_path)
