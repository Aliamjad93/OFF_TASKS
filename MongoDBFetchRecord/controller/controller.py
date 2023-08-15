from mongo.db import Database
from bson.objectid import ObjectId

class Controller:
    def Main():
        return ({'record': 'Hello World'})
    
    def Create_Data(Data):
        Data=dict(Data)
        Database.insert_one(Data)
        return {"message": 'record added successfully'}
    
    def Get_Data():
        Response=Database.find()
        Records_List=[]
        
        for j in Response:
            Records_List.append(j)
        
        return Records_List
    
    def Data():
        DataFrame=Controller.Get_Data()
        
        return {'msg':f'{DataFrame}'} 
    
    def Get_Specific_Data(data):
        Target_Id = ObjectId(data)
    
        Record=Database.find_one({'_id':Target_Id})
    
        return str(Record)  
    

Contoller=Controller()





