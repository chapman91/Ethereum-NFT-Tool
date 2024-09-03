import json
import os

def update_metadata(metadata_folder, base_image_url):
    # Get a list of all files in the metadata folder and sort them
    filenames = sorted(os.listdir(metadata_folder))    
   
   
   
   
   
   
    # List all files in the metadata folder
    for i, filename in enumerate(filenames):
        if filename.endswith('.json'):
            # Construct the full path to the metadata file
            file_path = os.path.join(metadata_folder, filename)
            
            # Read the JSON data from the file
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            # Construct the image URL based on the index (i + 1)
            image_filename = f"image{i + 1}.png"  # Assuming images are .jpg, adjust if necessary
            new_image_url = base_image_url + image_filename

            # Update the 'image' key in the JSON data
            data['image'] = new_image_url
            
            # Write the updated JSON data back to the file
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)

# Main execution block
if __name__ == "__main__":
    metadata_folder = "./metadata_folder"
    base_image_url = "https://ipfs.io/ipfs/QmQ7jWzYbqVDf8eHHZuEddsFQtMs4bV4PD5YeWWZX8mg2r/"

    update_metadata(metadata_folder, base_image_url)
    
    print("Metadata updated.")
