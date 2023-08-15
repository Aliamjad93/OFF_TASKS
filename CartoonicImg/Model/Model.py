import cv2
import os

class cartoonize_image:

    def UploadPhoto(self,file):
        
        print(file.filename)
        # Load the image
        # # # Create a directory to store uploaded images if it doesn't exist
        upload_dir = "uploaded_imagess"
        os.makedirs(upload_dir, exist_ok=True)
    
        # # # # Save the image file to the upload directory
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path , "wb") as f:
            f.write(file.file.read())
            
            
        # #Now load the image
        img = cv2.imread(file_path)
        
        
        return img
    
    
    
    
model=cartoonize_image()