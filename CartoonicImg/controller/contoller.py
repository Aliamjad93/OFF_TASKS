import cv2
from Model.Model import model

class CartoonizedImage:
    def __init__(self):
        self.output_path=""
    def cartoonize_image(self,filename):
        # Load the image
        # img = cv2.imread(image_path)
        
        # Convert the image to grayscale
        img=model.UploadPhoto(filename)
        
        
        
        self.output_path = rf"C:\Users\farha\.spyder-py3\Task1\CartoonicImg\uploaded_imagess\gray_image.png"
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(self.output_path,gray)
        
       
        
    #     # Apply Gaussian blur to reduce noise and details
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Apply adaptive thresholding for edge detection
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 9, 9)
        
        # Apply bilateral filter to reduce noise while keeping edges sharp
        color = cv2.bilateralFilter(img, 9, 300, 300)
        cv2.imshow('Image',color)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Combine color image with edges to create a cartoon effect
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        
        
        
        # Save the cartoonized image
        self.output_path = rf"C:\Users\farha\.spyder-py3\Task1\CartoonicImg\uploaded_imagess\cartoonic_image.png"
        cv2.imwrite(self.output_path, cartoon)
        
        
        
    
    

# # # Replace these paths with your input and output image paths
# input_image_path = r"C:\Users\farha\OneDrive\Desktop\ali1.jpg"
# output_image_path = rf"C:\Users\farha\.spyder-py3\Task1\CartoonicImg\cartooniz_image.png"

# Perform the cartoonization
# cartoonize_image(input_image_path, output_image_path)

controller=CartoonizedImage()
