import os

# Specify the directory containing the photos
directory = r"C:\Users\mmste\Documents\size\raw"

# Get the list of files in the directory
files = os.listdir(directory)

# Define the starting number for renaming
start_number = 1

# Loop through each file in the directory
for file in files:
    # Construct the new filename
    new_filename = f"photo_{start_number}.jpg"  # Change the extension if your photos have a different format
    
    # Construct the full path for the old and new filenames
    old_path = os.path.join(directory, file)
    new_path = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(old_path, new_path)
    
    # Increment the start number
    start_number += 1
