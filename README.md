# NFT Image URL Updater

## Overview

NFT Image URL Updater is a Python script that allows you to dynamically update the image field in .json metadata files for an NFT collection. This is useful when you need to update the base URL of your NFT images (e.g., when moving images to a new hosting service). The script processes all .json files in a specified folder, updating each one’s image URL based on a provided base URL and file naming convention.


### Prerequisites

Python 3.x installed on your machine.
Your NFT collection's metadata in .json format, stored in a folder.

#### Installation

1. Clone or download this repository:

   `git clone https://github.com/yourusername/nft-url-updater.git`
   `cd nft-url-updater`



2. Prepare your metadata: Ensure your NFT metadata files are stored in a folder (e.g., ./ metadata_folder/) and that each .json file has an image field to update.


Usage

1. Open the Script: If you need to modify the script (e.g., change the image file extension), open update_urls.py in any text editor.

2. Run the Script: The script uses default values for the metadata folder and base image URL. To run it with the defaults, simply execute:

   - python update_urls.py

3. Adjust Configuration:
   If necessary, update the metadata_folder and base_image_url directly in the script:

    metadata_folder = "./metadata_folder"
    base_image_url = "https://ipfs.io/ipfs/QmYourNewBaseHash/"

4. Image Naming Convention: The script assumes your images follow a sequential naming pattern like image1.png, image2.png, etc.  If you use a different extension (e.g., .jpg), modify this line in update_urls.py:


    - image_filename = f"image{i + 1}.png"


###### Example

python update_urls.py
This will update the image field of all .json files in ./metadata_folder/ to use the base URL https://ipfs.io/ipfs/QmYourNewBaseHash/.