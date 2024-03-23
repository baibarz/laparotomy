import os
import hashlib
import shutil

def hash_file(filename):
    """Return the MD5 hash of the file."""
    hasher = hashlib.md5()
    with open(filename, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicates(directory):
    """Find and move duplicate files in the given directory."""
    hashes = {}
    duplicates = []

    # Create a folder for duplicates
    duplicates_folder = os.path.join(directory, "duplicates")
    if not os.path.exists(duplicates_folder):
        os.makedirs(duplicates_folder)

    # Iterate over all files in the directory
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            # Skip the duplicates folder itself
            if foldername == duplicates_folder:
                continue

            file_path = os.path.join(foldername, filename)
            file_hash = hash_file(file_path)

            # Check if the hash is already in the dictionary
            if file_hash in hashes and os.path.exists(hashes[file_hash]):
                print(f"Duplicate found: {filename}")
                duplicates.append(file_path)
                # Move duplicate to the duplicates folder
                shutil.move(file_path, duplicates_folder)
            else:
                hashes[file_hash] = file_path

    return duplicates

# Replace 'your_directory_path_here' with your directory path
duplicate_files = find_duplicates(r"C:\Users\mmste\Documents\size\download\ThirstForBeauty")
print(f"Found {len(duplicate_files)} duplicates which are moved to the duplicates folder.")
