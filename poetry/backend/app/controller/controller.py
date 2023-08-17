from app.mongo.db import Database  # Import your database module
from bson.objectid import ObjectId

class Controller:
    def Main():
        return {'record': 'Hello World'}  # Return a simple dictionary
    
    def Create_Data(Data):
        Data = dict(Data)  # Convert input data to a dictionary
        Database.insert_one(Data)  # Insert data into the database
        
        return {"message": 'record added successfully'}
    
    def Get_Data():
        Response = Database.find()  # Retrieve data from the database
        
        Records_List = []
        for record in Response:   # applying loop to fetch data from Objects by ObjectId
            
            record_dict = dict(record) #converting data into dictionary for returning record into json
            if "_id" in record_dict:
                record_dict["_id"] = str(record_dict["_id"])  # Convert ObjectId to string
            Records_List.append(record_dict)  # Append processed record to the list
        
        return Records_List
    
    def Get_Specific_Data(data):
        Target_Id = ObjectId(data)  # Convert input data to ObjectId
    
        Record = Database.find_one({'_id': Target_Id})  # Retrieve a specific record
    
        return str(Record)  # Return the retrieved record as a string
    
# Create an instance of the Controller class
Controller_Instance = Controller()
