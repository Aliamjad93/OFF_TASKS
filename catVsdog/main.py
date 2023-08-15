# # # import opendatasets as od

# # # od.download("https://www.kaggle.com/datasets/salader/dogs-vs-cats/data","C:/Users/farha/.spyder-py3/catVsdog")



# import tensorflow as tf
# from tensorflow import keras
# from keras import Sequential
# # from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten


# # # ... (previous code)








# # train_ds=keras.utils.image_dataset_from_directory(directory='C:/Users/farha/.spyder-py3/catVsdog/dogs-vs-cats/train',
# #                                           labels='inferred',
# #                                           label_mode='int',
# #                                           batch_size=32,
# #                                           image_size=(256,256))

# # val_ds=keras.utils.image_dataset_from_directory(directory='C:/Users/farha/.spyder-py3/catVsdog/dogs-vs-cats/test',
# #                                           labels='inferred',
# #                                           label_mode='int',
# #                                           batch_size=32,
# #                                           image_size=(256,256))



# # #Normalize Data


# # def process(image,label):
# #     image=tf.cast(image/255. , tf.float32)
# #     return image,label


# # train_ds=train_ds.map(process)
# # val_ds=val_ds.map(process)



# # #Create CNN Model
# # model=Sequential()
# # model.add(Conv2D(32, kernel_size=(3,3),padding='valid',activation='relu',input_shape=(256,256,3)))
# # model.add(MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'))



# # model.add(Conv2D(64, kernel_size=(3,3),padding='valid',activation='relu'))
# # model.add(MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'))



# # model.add(Conv2D(128, kernel_size=(3,3),padding='valid',activation='relu'))
# # model.add(MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'))

# # model.add(Flatten())

# # model.add(Dense(128, activation='relu'))
# # model.add(Dense(64, activation='relu'))
# # model.add(Dense(1, activation='sigmoid'))



# # model.summary()


# # # #evaluatiom

# # model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])



# # # #training


# # history=model.fit(train_ds,epochs=8,validation_data=val_ds)










# # #plotting





# # import matplotlib.pyplot as plt
# # # plt.plot(history.history['accuracy'],color='red',label='train')
# # # plt.plot(history.history['val_accuracy'],color='blue',label='validation')




# # plt.plot(history.history['loss'],color='red',label='train')
# # plt.plot(history.history['val_loss'],color='blue',label='validation')



# # Save the trained model
# # model.save("catVsdog.h5")









# # from fastapi import FastAPI, UploadFile, File, HTTPException
# # from fastapi.responses import JSONResponse
# # from pydantic import BaseModel
# # import imghdr
# # import os

# # app = FastAPI()

# # # class ImageForm(BaseModel):
# # #     labels: str

# # @app.post("/upload/")
# # async def upload_file(file: UploadFile = File(...)):
# #     # Check if the uploaded file is a JPG image
# #     # if imghdr.what(None, file.file.read()) != "jpeg":
# #     #     raise HTTPException(status_code=400, detail="Only JPG images are allowed")

# #     # Handle the uploaded image file
# #     # Save the image file, process it, etc.
# #     # file.file.read() to access the file content
    
    
# #     # Create a directory to store uploaded images if it doesn't exist
# #     upload_dir = "uploaded_images"
# #     os.makedirs(upload_dir, exist_ok=True)

# #     # Save the image file to the upload directory
# #     file_path = os.path.join(upload_dir, file.filename)
# #     with open(file_path, "wb") as f:
# #         f.write(file.file.read())
    
# #     print(file_path)


    
# #     loaded_model = keras.models.load_model("my_model.h5")


    
    
# #     import cv2
    
# #     img=cv2.imread(rf'{file_path}')
    
    
# #     test_img=cv2.resize(img,(256,256))
    
    
# #     test_input=test_img.reshape((1,256,256,3))
    
    
# #     if loaded_model.predict(test_input)>0.5:
        
# #         #     # Return a response indicating success
        
# #         return JSONResponse(content={"message": "The Object in image is -- DOG"})
# #     else:
# #         return JSONResponse(content={"message": "The Object in image is -- CAT"})





# from fastapi import FastAPI, UploadFile, File, HTTPException
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
# import imghdr
# import os

# app = FastAPI()

# # Pydantic model for the file upload request
# class ImageUpload(BaseModel):
#     file: UploadFile = File(...)

# @app.post("/upload/")
# async def upload_file(payload: UploadFile=File(...)):
#     file = payload.file

#     # Check if the uploaded file is a JPG image
#     # if imghdr.what(None, file.file.read()) != "jpeg":
#         # raise HTTPException(status_code=400, detail="Only JPG images are allowed")

#     # Handle the uploaded image file
#     # Save the image file, process it, etc.
    
#     # Create a directory to store uploaded images if it doesn't exist
#     upload_dir = "uploaded_images"
#     os.makedirs(upload_dir, exist_ok=True)

#     # Save the image file to the upload directory
#     file_path = os.path.join(upload_dir, file.filename)
#     with open(file_path, "wb") as f:
#         f.write(file.file.read())
    
#     return {"message": "File uploaded successfully", "file_path": file_path}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)






    


















































from routes.Routes import route
import uvicorn



if __name__=='__main__':
    uvicorn.run(route.app,host="127.0.0.1",port=8000)


    





























