import os
import numpy as np
from PIL import Image
from sklearn.neighbors import KDTree

def average_color(image):
    """ Calculate the average color of an image. """
    return np.mean(np.mean(image, axis=0), axis=0)

def load_photos_from_folder(folder_path, image_size):
    """ Load photos from a folder and resize them. """
    photos = []
    for filename in os.listdir(folder_path):
        try:
            img_path = os.path.join(folder_path, filename)
            with Image.open(img_path) as img:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img = img.resize(image_size)
                photos.append(img)
        except Exception as e:
            print(f"Skipping {filename}: {e}")
    return photos

def create_photo_mosaic(target_image_path, photo_list, grid_size):
    """ Create a photo mosaic with unique photos for each grid cell. """
    target_image = Image.open(target_image_path)
    target_image = target_image.resize(grid_size)
    target_image = np.array(target_image)
    
    rows, cols, _ = target_image.shape

    mosaic_image = Image.new('RGB', (cols * 100, rows * 100))

    photo_colors = np.array([average_color(np.array(photo)) for photo in photo_list])
    tree = KDTree(photo_colors)

    used_indices = set()
    for y in range(rows):
        for x in range(cols):
            color = target_image[y, x]
            dist, index = tree.query([color], k=len(photo_list))
            for idx in index[0]:
                if idx not in used_indices:
                    used_indices.add(idx)
                    photo = photo_list[idx]
                    mosaic_image.paste(photo, (x * 100, y * 100))
                    break

    return mosaic_image

folder_path = r"C:\Users\mmste\Documents\size\raw"  
photos = load_photos_from_folder(folder_path, (100, 100))


target_image_path = r"C:\Users\mmste\Documents\size\testphotos\yaser.jpg"  
mosaic = create_photo_mosaic(target_image_path, photos, (88, 100))


mosaic.save('bro10.TIF')
