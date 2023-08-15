import pymongo

try:
    # Try to establish the connection to MongoDB
    Client = pymongo.MongoClient('mongodb://localhost:27017')
    MyDb = Client['Student']
    Database = MyDb['stdinfo']

    print("Connection to MongoDB established successfully.")
except pymongo.errors.ServerSelectionTimeoutError as e:
    print(f"Error: Could not connect to MongoDB. {e}")
