    
#importing required modules
from model.Model import fileupload

class Controller:
        
        
        
        # Make Predictions making a function which take input as an image 
    def predict(self,filename):

        return fileupload.upload_file(filename)
        
obj_contoller=Controller()






























