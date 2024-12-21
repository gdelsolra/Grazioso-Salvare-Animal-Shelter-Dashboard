import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps # Handles MongoDB-specific types

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33830
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        """
        Insert a document into the MongoDB collection.
        :param data: Dictionary containing the document data.
        :return: A sucess message with summary of the inserted data,
        or False if insertion fails.
        """
        if isinstance(data, dict): #Validate that data is a dictionary
            try:
                result = self.database.animals.insert_one(data)  # data should be dictionary            
                animal_type = data.get("animal_type", "Unknown animal")
                return f"{animal_type} has been inserted successfully"
            except Exception as e:
                print(f"An error occurred during insertion: {e}")
                return False
        else:
            raise TypeError("Data to insert must be a dictionary")
# Create method to implement the R in CRUD.
    def read(self, query):
        """
        Query documents from the MongoDB collection.
        :param query: Dictionary containing the query parameters.
        :return: List of documents matching the query, or an empty list if none found.
        """ 
        if isinstance(query, dict):
            try:
                #Use the query to find documents in the collection
                results = self.database.animals.find(query)
                
                # Convert the MongoDB cursor into a list of documents
                documents = list(results)
                
                #Just return the documents. Do not print everything.
                return documents if documents else[]
                
            except Exception as e:
                print(f"An error occurred during query:{e}")
                return[]
            
#Create method to implement the U in CRUD.
    def update(self, query, updates):
        """
        Update documents in the MongoDB collection.
        :param:
            query(dict): The key-value lookup pair for filtering.
            updates(dict): The key-value pairs to update in the matched documents.
        :return:
            int: The number of documents updated.
        """
        try:
            if query and updates and isinstance(query, dict) and isinstance(updates, dict):
                result = self.database.animals.update_one(query,{'$set':updates})
                return result.modified_count
            else:
                raise ValueError("Both query and updates must be non-empty dictionaries.")
        except Exception as e:
            print(f"Error in update method:{e}")
            return 0
    #Create method to implement the D in CRUD
    def delete(self, query):
        """
        Delete documents from the MongoDB collection.
        :param:
            query(dict): The key-value lookup pair for filtering.
        :return:
            int: the number of documents deleted.
        """
        try:
            if query and isinstance(query, dict):
                results = self.database.animals.delete_one(query)
                if results.deleted_count > 0:
                    return f"Document(s) successfully deleted. Deleted count:{results.deleted_count}"
                else:
                    return "No documents found. Nothing was deleted."
            else:
                raise ValueError("Query must be a non-empty dictionary.")
        except Exception as e:
            print(f"Error in delete method: {e}")
            return 0







