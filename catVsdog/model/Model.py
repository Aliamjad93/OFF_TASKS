from fastapi import UploadFile, File, HTTPException
from tensorflow import keras
from fastapi.responses import JSONResponse
import os



class FileUploadService:
    
    
        
    def upload_file(self,file):
        

        
        
        # # # Create a directory to store uploaded images if it doesn't exist
        upload_dir = "uploaded_imagess"
        os.makedirs(upload_dir, exist_ok=True)
    
        # # # Save the image file to the upload directory
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        
    
        
        loaded_model = keras.models.load_model(r"C:\Users\farha\.spyder-py3\catVsdog\my_model.h5")
    
        
        print(file_path)
        
        
        import cv2
        
        img=cv2.imread(rf'{file_path}')
        
        
        test_img=cv2.resize(img,(256,256))
        
        
        test_input=test_img.reshape((1,256,256,3))
        # print(test_input)
        
        if loaded_model.predict(test_input)>0.5:
            
            
        # #     #     # Return a response indicating success
            
            return (JSONResponse(content={"message": "The Object in image is -- DOG"}))
        else:
            return ( JSONResponse(content={"message": "The Object in image is -- CAT"}))
        
        
        
fileupload=FileUploadService()
