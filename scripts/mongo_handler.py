from pymongo import MongoClient

class MongoDBGeoHandler:
    def __init__(self, db_name, collection_name, score_column_name=None):
        """
        Initialize the MongoDBGeoHandler with a MongoDB connection URI, database name, collection name,
        and an optional score column name.

        Parameters:
        db_name (str): The name of the database.
        collection_name (str): The name of the collection.
        score_column_name (str or None): The name of the score column to include in operations.
        """
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.score_column_name = score_column_name

    def count_all_records(self):
        """
        Count all records in the collection.

        Returns:
        int: The total number of documents in the collection.
        """
        return self.collection.count_documents({})

    def insert_data(self, df):
        """
        Insert data from a DataFrame into MongoDB with geospatial indexing.
        Assumes DataFrame columns 'latitude' and 'longitude' are present.
        """
        if self.score_column_name and self.score_column_name not in df.columns:
            raise ValueError(f"DataFrame is missing '{self.score_column_name}' column.")

        df['location'] = df.apply(lambda row: {
            'type': 'Point',
            'coordinates': [row['longitude'], row['latitude']]
        }, axis=1)

        data = df.to_dict(orient='records')
        self.collection.drop()  # Optionally drop the collection to start fresh
        result = self.collection.insert_many(data)
        self.collection.create_index([('location', '2dsphere')])

        print(f"Data inserted. Total documents: {len(result.inserted_ids)}")

    def count_records_within_radius(self, center_latitude, center_longitude, radius_meters):
        """
        Perform a geospatial query to count records within a given radius and compute the average score if applicable.
        """
        pipeline = [
            {'$geoNear': {
                'near': {'type': 'Point', 'coordinates': [center_longitude, center_latitude]},
                'distanceField': 'distance',
                'spherical': True,
                'maxDistance': radius_meters
            }}
        ]
        if self.score_column_name:
            pipeline.append({
                '$group': {
                    '_id': None,
                    'count': {'$sum': 1},
                    'average_score': {'$avg': f'${self.score_column_name}'}
                }
            })
        else:
            pipeline.append({'$group': {'_id': None, 'count': {'$sum': 1}}})

        result = list(self.collection.aggregate(pipeline))
        if result:
            return {'count': result[0]['count'], 'average_score': result[0].get('average_score')}
        else:
            return {'count': 0, 'average_score': None}
