from PIL import Image
import os

def resize_images(input_dir, output_dir, size=(150, 100)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        try:
            with Image.open(os.path.join(input_dir, filename)) as img:
                img.thumbnail(size, Image.LANCZOS)
                img.save(os.path.join(output_dir, filename))
                print(f"{filename} resized successfully")
        except Exception as e:
            print(f"Error resizing {filename}: {str(e)}")

if __name__ == "__main__":
    input_dir = r"C:\Users\mmste\Documents\size\download"
    output_dir = r"C:\Users\mmste\Documents\size\download\150"
    resize_images(input_dir, output_dir)
