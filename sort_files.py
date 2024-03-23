import os
import shutil
import time
from PIL import Image
import moviepy.editor as mp

def is_video(file_path):
    return file_path.lower().endswith(('.mp4', '.mov', '.avi'))

def is_image(file_path):
    return file_path.lower().endswith(('.png', '.jpg', '.jpeg'))

def move_file_with_retry(src, dst, attempts=5, delay=1):
    for attempt in range(attempts):
        try:
            shutil.move(src, dst)
            print(f"Moved {src} to {dst}")
            break
        except PermissionError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    else:
        print(f"Failed to move {src} after {attempts} attempts")

def sort_files(folder_path):
    photos_path = os.path.join(folder_path, "Photos")
    videos_path = os.path.join(folder_path, "Videos")

    if not os.path.exists(photos_path):
        os.makedirs(photos_path)

    if not os.path.exists(videos_path):
        os.makedirs(videos_path)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            if is_image(file_path):
                move_file_with_retry(file_path, os.path.join(photos_path, file))
            elif is_video(file_path):
                move_file_with_retry(file_path, os.path.join(videos_path, file))

sort_files(r"C:\Users\mmste\Documents\done\TimeSea")
