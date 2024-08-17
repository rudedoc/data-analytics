from pymongo import MongoClient

class MongoDBGeoHandler:
    def __init__(self, mongo_uri='mongodb://localhost:27017/'):
        """
        Initialize the MongoDBGeoHandler with a MongoDB connection URI.

        Parameters:
        mongo_uri (str): The MongoDB connection URI.
        """
        self.mongo_uri = mongo_uri
        self.client = MongoClient(mongo_uri)

    def insert_data(self, df, db_name, collection_name):
        """
        Insert data from a DataFrame into MongoDB with geospatial indexing.

        Parameters:
        df (DataFrame): The DataFrame containing the data to insert.
        db_name (str): The name of the database.
        collection_name (str): The name of the collection.
        """
        # Check if the DataFrame contains 'latitude' and 'longitude' columns
        required_columns = ['latitude', 'longitude']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"DataFrame is missing required column: '{col}'")

        # Combine latitude and longitude into GeoJSON format for MongoDB
        df['location'] = df.apply(lambda row: {
            'type': 'Point',
            'coordinates': [row['longitude'], row['latitude']]
        }, axis=1)

        # Convert the DataFrame to a list of dictionaries
        data = df.to_dict(orient='records')

        # Specify the database and collection
        db = self.client[db_name]
        collection = db[collection_name]

        # Drop the collection if it exists to start fresh (optional)
        collection.drop()

        # Insert the data into the collection and get the insert count
        result = collection.insert_many(data)
        insert_count = len(result.inserted_ids)

        # Create a geospatial index on the location field
        collection.create_index([('location', '2dsphere')])

        print(f"Data has been successfully inserted into MongoDB in the '{db_name}' database, '{collection_name}' collection.")
        print(f"Total documents inserted: {insert_count}")

    def count_records_within_radius(self, db_name, collection_name, center_latitude, center_longitude, radius_meters):
        """
        Count the number of records within a specified radius of a given latitude and longitude.

        Parameters:
        db_name (str): The name of the database.
        collection_name (str): The name of the collection.
        center_latitude (float): The latitude of the center point.
        center_longitude (float): The longitude of the center point.
        radius_meters (float): The radius in meters within which to search for records.

        Returns:
        int: The count of records found within the specified radius.
        """
        # Specify the database and collection
        db = self.client[db_name]
        collection = db[collection_name]

        # Define the aggregation pipeline
        pipeline = [
            {
                '$geoNear': {
                    'near': {'type': 'Point', 'coordinates': [center_longitude, center_latitude]},
                    'distanceField': 'distance',
                    'spherical': True,
                    'maxDistance': radius_meters  # Use the radius in meters directly
                }
            },
            {
                '$count': 'count'  # Count the number of documents found
            }
        ]

        # Execute the aggregation
        result = list(collection.aggregate(pipeline))

        # Return the count if result is found, else return 0
        if result:
            return result[0]['count']
        else:
            return 0
