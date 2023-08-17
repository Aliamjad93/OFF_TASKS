# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:29:24 2023

@author: farha
"""
# Importing required modules
from fastapi import FastAPI
from fastapi import UploadFile, File
from controller.contoller import controller  # Importing the 'controller' instance from 'controller' module

# Creating a class called 'Router'
class Router:
    # Creating an instance of 'FastAPI'
    app = FastAPI()
    
    # Defining a route for the root URL '/'
    @app.get('/')
    def index():
        return {'message': 'Welcome to Conversion Image into Cartoon App'}
    
    # Defining a route for the '/cartoonic' endpoint using HTTP POST method
    @app.post('/cartoonic')
    def Cartoon(file: UploadFile = File(...)):
        # Calling the 'cartoonize_image' method from the 'controller' instance
        controller.cartoonize_image(file)
        return {"message": 'Image is Converted, Check Your Directory'}

# Creating an instance of the 'Router' class
router = Router()
