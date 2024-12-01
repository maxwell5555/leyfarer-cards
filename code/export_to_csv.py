import csv
import json
import os

# Function to read JSON from a file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)  # Load the JSON data into a Python object
    return data

# Function to read and process all JSON files in a directory
def process_all_json_files(directory, writer, selected_items):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):  # Check for JSON files
            file_path = os.path.join(directory, filename)
            try:
                data = read_json_file(file_path)
                process_json_data(data, filename, writer, selected_items)  # Call the processing function
            except FileNotFoundError:
                print(f"File not found: {file_path}")
            except json.JSONDecodeError:
                print(f"Error decoding JSON from file: {file_path}")

# Function to process each JSON file
def process_json_data(data, filename, writer, selected_items):
    print(f"Processing {filename}")
    # Replace this with your actual processing logic

    item = {}
    item['name'] = data['data']['children'][1]['children'][0]['text']
    item['type'] = data['data']['children'][1]['children'][1]['text']
    item['info'] = data['data']['children'][1]['children'][2]['text']
    item['rarity'] = data['data']['children'][1]['children'][3]['text']
    item['stats'] = data['data']['children'][1]['children'][4]['text']
    item['price'] = "$1.00"
    item['image'] = item['name'] + '.png'

    data = [item['name'], item['type'], item['price'], item['image']]

    writer.writerow(data)  # Write the selected data
    print(item)

if __name__ == "__main__":
    directory_path = 'items'  # Replace with your JSON file path

    # Define the CSV filename
    csv_filename = 'selected_data.csv'

    # Create a list of selected items from the dictionary
    selected_items = ['name', 'type', 'price', 'image']

    # Writing selected items to CSV
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, selected_items)
        writer.writerow(selected_items)  # Write the header (column names)
        

        process_all_json_files(directory_path, writer, selected_items)