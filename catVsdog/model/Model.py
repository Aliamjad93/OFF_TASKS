#importing required modules
from tensorflow import keras
from fastapi.responses import JSONResponse
import os
import cv2



class FileUploadService:
    
    
        
    def upload_file(self,file):
        

        
        
        # # # Create a directory to store uploaded images if it doesn't exist
        upload_dir = "uploaded_imagess"
        os.makedirs(upload_dir, exist_ok=True)
    
        # # # Save the image file to the upload directory
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        
    
        #Load model to make predictions
        loaded_model = keras.models.load_model(r"C:\Users\farha\.spyder-py3\Task1\catVsdog\my_model.h5")
        
        
        
        # reading image from the file path variable.
        img=cv2.imread(rf'{file_path}')
        
        # resizing image into 256,256 
        test_img=cv2.resize(img,(256,256))
        
        # Reshaping the test_img array to match the expected input shape of the model
        # The original shape of test_img is (256, 256, 3), representing a single image with dimensions 256x256 and 3 color channels (RGB)
        # The model expects a batch of images as input, so we reshape it to (1, 256, 256, 3)
        # The first dimension (1) indicates that there is one image in the batch
        # The second and third dimensions (256, 256) are the image dimensions
        # The fourth dimension (3) represents the number of color channels (RGB)
        test_input=test_img.reshape((1,256,256,3))
        # print(test_input)
        
        if loaded_model.predict(test_input)>0.5:
            
            
        # #     #     # Return a response indicating success
            
            return (JSONResponse(content={"message": "The Object in image is -- DOG"}))
        else:
            return ( JSONResponse(content={"message": "The Object in image is -- CAT"}))
        
        
        
fileupload=FileUploadService()
