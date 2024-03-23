import os
import torch
from tqdm import tqdm
import easyocr
import shutil

# Check if CUDA is available
if torch.cuda.is_available():
    print("CUDA is available. GPU support is enabled.")
else:
    print("CUDA is not available. GPU support is disabled. Running on CPU.")

# Set device to GPU if available
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Path to the folder containing your images
images_folder = r"E:\download done photos\TimeSea\Photos"  # Update this with your actual folder path

# Path to the folder where you want to save images with text
text_folder = os.path.join(images_folder, "text")

# Path to the folder where you want to save images without text
no_text_folder = os.path.join(images_folder, "no_text")

# Create necessary folders if they don't exist
for folder in [text_folder, no_text_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function to check if the image contains text using easyocr
def has_text(image_path):
    try:
        reader = easyocr.Reader(['en'], gpu=device)  # Use GPU
        results = reader.readtext(image_path)
        return len(results) > 0
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return False

# Loop through each image in the folder
for filename in tqdm(os.listdir(images_folder)):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(images_folder, filename)
        if has_text(image_path):
            # Move image to text folder
            shutil.move(image_path, os.path.join(text_folder, filename))
        else:
            # Move image to no text folder
            shutil.move(image_path, os.path.join(no_text_folder, filename))

print(torch.cuda.current_device())
print("Text recognition and sorting completed.")
