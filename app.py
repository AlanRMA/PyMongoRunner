from pymongo import MongoClient
import os


class MongoObject:
    def __init__(self, URI):
        self.client = MongoClient(URI)

    def createCollection(self, dbName, collectionName):
        db = self.client[dbName]
        db.create_collection(collectionName)
        print(f"Collection '{collectionName}' created in database '{dbName}'.")

    def deleteCollection(self, dbName, collectionName):
        db = self.client[dbName]
        db.drop_collection(collectionName)
        print(f"Collection '{collectionName}' deleted from database '{dbName}'.")

    def addData(self, dbName, collectionName, data):
        db = self.client[dbName]
        db[collectionName].insert_one(data)
        print(f"Data added to collection '{collectionName}' in database '{dbName}'.")

    def removeData(self, dbName, collectionName, query):
        db = self.client[dbName]
        deleted_count = db[collectionName].delete_many(query).deleted_count
        print(f"{deleted_count} document(s) deleted from collection '{collectionName}' in database '{dbName}'.")

    def query(self, dbName, collectionName, query):
        db = self.client[dbName]
        cursor = db[collectionName].find(query)
        for document in cursor:
            print(document)
        return cursor 

    def close(self):
        self.client.close()

    def __del__(self):
        self.close()


def main():
    # Example of usage
    URI = os.getenv("MONGO_CONNECTION_STRING") # replace with your MongoDB URI
    dbName = "testDB"
    collectionName = "testCollection"
    data = {"name": "John Doe", "age": 29, "city": "New York"}

    # Initialize MongoObject
    mongo = MongoObject(URI)

    # Create collection
    mongo.createCollection(dbName, collectionName)

    # Add data to collection
    mongo.addData(dbName, collectionName, data)

    # Query data from collection
    query_result = mongo.query(dbName, collectionName, {"name": "John Doe"})
    for doc in query_result:
        print(doc)
if __name__ == "__main__":
    main()
