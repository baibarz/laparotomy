import os
from PIL import Image


def is_square(image_path):
  """Checks if an image is square."""
  img = Image.open(image_path)
  width, height = img.size
  return width == height


def sort_photos(source_dir, square_dir="square_photos", non_square_dir="non_square_photos"):
  """Sorts photos in a directory into square and non-square folders."""
  os.makedirs(os.path.join(source_dir, square_dir), exist_ok=True)
  os.makedirs(os.path.join(source_dir, non_square_dir), exist_ok=True)

  for filename in os.listdir(source_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
      image_path = os.path.join(source_dir, filename)
      if is_square(image_path):
        dest_dir = os.path.join(source_dir, square_dir)
      else:
        dest_dir = os.path.join(source_dir, non_square_dir)
      os.rename(image_path, os.path.join(dest_dir, filename))


# Replace with your directory path
source_dir = r"C:\Users\mmste\Documents\size\download\music\el"
sort_photos(source_dir)

print("Photos sorted successfully!")
