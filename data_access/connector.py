from pymongo import MongoClient

class MongoDBConnector:
    """
    Handles MongoDB connections and operations.

    Attributes:
        client: MongoClient object for connecting to MongoDB.
        db: Reference to the MongoDB database.
    """

    def __init__(self, uri, db_name):
        """
        Initialize the MongoDBConnector.

        Args:
            uri (str): The MongoDB connection URI.
            db_name (str): The database name.

        Raises:
            ConnectionError: If the connection to MongoDB fails.
        """
        try:
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
        except Exception as e:
            raise ConnectionError(f"Failed to connect to MongoDB: {str(e)}")

    def get_collection(self, collection_name):
        """
        Retrieve a MongoDB collection.

        Args:
            collection_name (str): The name of the collection.

        Returns:
            Collection: The MongoDB collection object.

        Raises:
            ValueError: If the collection cannot be accessed.
        """
        try:
            return self.db[collection_name]
        except Exception as e:
            raise ValueError(f"Error accessing collection: {str(e)}")
