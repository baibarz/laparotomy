from PIL import Image
import os

# Define the directory containing your photos
photos_directory = r"C:\Users\mmste\Documents\size\raw"

# Define the rotation angle
rotation_angle = 90

# Get a list of all files in the directory
photo_files = os.listdir(photos_directory)

# Iterate through each file
for photo_file in photo_files:
    # Check if the file is an image
    if photo_file.endswith(".jpg") or photo_file.endswith(".png") or photo_file.endswith(".jpeg"):
        try:
            # Open the image
            image_path = os.path.join(photos_directory, photo_file)
            image = Image.open(image_path)

            # Rotate the image
            rotated_image = image.rotate(rotation_angle, expand=True)

            # Save the rotated image, overwrite the original file
            rotated_image.save(image_path)

            print(f"Rotated {photo_file} successfully.")
        except Exception as e:
            print(f"Error rotating {photo_file}: {e}")
    else:
        print(f"{photo_file} is not an image file.")
