import cv2
import os
import shutil
from PIL import Image
from pathlib import Path

def view_and_sort_files(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    Path(destination_folder).mkdir(parents=True, exist_ok=True)

    # List all files in the source folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    for file in files:
        file_path = os.path.join(source_folder, file)

        # Check if the file is an image or a video
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tif', '.tiff')):
            # Display image
            with Image.open(file_path) as img:
                img.show()

        elif file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv')):
            # Display first frame of the video
            cap = cv2.VideoCapture(file_path)
            ret, frame = cap.read()
            if ret:
                cv2.imshow('Video Frame', frame)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            cap.release()

        print(f"Viewing: {file}")
        print("Press Enter to move this file to the 'liked' folder, or any other key to continue.")
        
        # Wait for user input
        key = input()
        if key == '':
            # Move file to liked folder
            shutil.move(file_path, os.path.join(destination_folder, file))
            print(f"Moved: {file}")

    print("All files have been processed.")

# Change these paths to your specific folders
source_folder = 'path/to/your/source/folder'
destination_folder = 'path/to/your/liked/folder'

view_and_sort_files(source_folder, destination_folder)
