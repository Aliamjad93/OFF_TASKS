# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:29:24 2023

@author: farha
"""
from fastapi import FastAPI
from fastapi import UploadFile, File
from controller.contoller import controller

class Router:
    app=FastAPI()
    
    
    @app.get('/')
    def index():
        return {'message':'Welcome to Conversion Image into Cartoon App'}
        # return view.html
    
    @app.post('/cartoonic')
    def Cartoon(file: UploadFile= File(...)):
        # print(file.filename)
        controller.cartoonize_image(file)
        return {"message": 'Image is Converted, Check Your Directory'}
        
    
        
        
        
router=Router()