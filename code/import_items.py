import json
from pymongo import MongoClient
import os

# Function to read JSON from a file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)  # Load the JSON data into a Python object
    return data

# Function to process each JSON file
def process_json_data(data, filename, client):
    print(f"Processing {filename}")
    # Replace this with your actual processing logic

    item = {}
    item['name'] = data['data']['children'][1]['children'][0]['text']
    item['type'] = data['data']['children'][1]['children'][1]['text']
    item['info'] = data['data']['children'][1]['children'][2]['text']
    item['rarity'] = data['data']['children'][1]['children'][3]['text']
    item['stats'] = data['data']['children'][1]['children'][4]['text']
    
    # Define the database and collection names
    database_name = 'LEYFARERS'  # Replace with your database name
    collection_name = 'ITEMS'  # Replace with your collection name

    # Insert the dictionary into the database
    insert_dictionary(client, database_name, collection_name, item)
    #print(item)



# Function to read and process all JSON files in a directory
def process_all_json_files(directory, client):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):  # Check for JSON files
            file_path = os.path.join(directory, filename)
            try:
                data = read_json_file(file_path)
                process_json_data(data, filename, client)  # Call the processing function
            except FileNotFoundError:
                print(f"File not found: {file_path}")
            except json.JSONDecodeError:
                print(f"Error decoding JSON from file: {file_path}")

# Function to insert a dictionary into MongoDB
def insert_dictionary(client, db_name, collection_name, data):
    # Access the database
    db = client[db_name]
    
    # Access the collection
    collection = db[collection_name]
    
    # Insert the dictionary into the collection
    result = collection.insert_one(data)
    
    # Print the inserted document's ID
    print(f"Inserted document ID: {result.inserted_id}")

if __name__ == "__main__":
    # Connect to MongoDB (default is localhost on port 27017)
    client = MongoClient('mongodb://oci-ampere.ts.soincompatible.com:27017/')

    directory_path = 'items'  # Replace with your JSON file path
    process_all_json_files(directory_path, client)
