from fastapi import UploadFile, File, HTTPException
from tensorflow import keras
from fastapi.responses import JSONResponse
import cv2
import os



class ModelPredictor:
    
    def __init__(self, model_path):
        self.loaded_model = keras.models.load_model(model_path)
    def predictPic(self,file_path):
        img=cv2.imread(rf'{file_path}')
        
        test_img=cv2.resize(img,(256,256))
                
                
        test_input=test_img.reshape((1,256,256,3))
                # print(test_input)
                
        if self.loaded_model.predict(test_input)>0.5:
                    
                    
                # #     #     # Return a response indicating success
                    
            return "DOG"
        else:
            return "CAT"
class ImageUploader:
    def __init__(self):
        self.upload_dir = "uploaded imagess"
        
        os.makedirs(self.upload_dir, exist_ok=True)

    def upload(self, file):
        file_path = os.path.join(self.upload_dir, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return file_path


class FileUploadService:
    def __init__(self, model_path):
        self.model_predictor = ModelPredictor(model_path)
        self.image_uploader = ImageUploader()

    def upload_file(self, file: UploadFile=File(...)):
        file_path = self.image_uploader.upload(file)
        # img = cv2.imread(file_path)
        
        prediction = self.model_predictor.predictPic(file_path)

        return JSONResponse(content={"message": f"The Object in image is -- {prediction}"})


# Example usage

model_path = r"C:\Users\farha\.spyder-py3\singleResponsibility\my_model.h5"
    
file_upload_service = FileUploadService(model_path)








