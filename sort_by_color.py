import cv2
import os

def is_mostly_red(image_path, threshold_percentage=35):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper bounds for red in HSV
    lower_red = (0, 50, 50)
    upper_red = (10, 255, 255)
    
    # Threshold the image to extract red regions
    mask = cv2.inRange(hsv_image, lower_red, upper_red)
    
    # Calculate the percentage of red pixels
    total_pixels = mask.size
    red_pixels = cv2.countNonZero(mask)
    percentage_red = (red_pixels / total_pixels) * 100
    
    # Check if the percentage of red pixels exceeds the threshold
    return percentage_red >= threshold_percentage

def is_mostly_blue(image_path, threshold_percentage=2):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper bounds for blue in HSV
    lower_blue = (110, 50, 50)
    upper_blue = (130, 255, 255)
    
    # Threshold the image to extract blue regions
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    
    # Calculate the percentage of blue pixels
    total_pixels = mask.size
    blue_pixels = cv2.countNonZero(mask)
    percentage_blue = (blue_pixels / total_pixels) * 100
    
    # Check if the percentage of blue pixels exceeds the threshold
    return percentage_blue >= threshold_percentage

def is_mostly_green(image_path, threshold_percentage=35):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper bounds for green in HSV
    lower_green = (12, 25, 25)
    upper_green = (86, 255, 255)
    
    # Threshold the image to extract green regions
    mask = cv2.inRange(hsv_image, lower_green, upper_green)
    
    # Calculate the percentage of green pixels
    total_pixels = mask.size
    green_pixels = cv2.countNonZero(mask)
    percentage_green = (green_pixels / total_pixels) * 100
    
    # Check if the percentage of green pixels exceeds the threshold
    return percentage_green >= threshold_percentage

def is_black_and_white(image_path, threshold_percentage=3):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate the percentage of non-white pixels
    total_pixels = gray_image.size
    white_pixels = cv2.countNonZero(cv2.threshold(gray_image, 250, 255, cv2.THRESH_BINARY)[1])
    percentage_white = (white_pixels / total_pixels) * 100
    
    # Check if the percentage of non-white pixels exceeds the threshold
    return percentage_white >= threshold_percentage

def move_photos_by_color(input_folder, output_folder, is_mostly_color_func, color_name):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Iterate over each file
    for file_name in files:
        # Construct the input file path
        input_path = os.path.join(input_folder, file_name)
        
        try:
            if is_mostly_color_func(input_path):
                # Move the file to the output folder
                os.rename(input_path, os.path.join(output_folder, file_name))
                print(f"Moved {file_name} to {output_folder}")
        except Exception as e:
            print(f"Error processing {file_name}: {str(e)}")

# Specify input and output folders
input_folder = r"C:\Users\mmste\Documents\size\download\art\TimeSea\Photos\no_text"
output_folder_red = r"C:\Users\mmste\Documents\size\download\art\TimeSea\Photos\red"
output_folder_blue = r"C:\Users\mmste\Documents\size\download\art\TimeSea\Photos\blue"
output_folder_green = r"C:\Users\mmste\Documents\size\download\art\TimeSea\Photos\green"
output_folder_bw = r"C:\Users\mmste\Documents\size\download\art\TimeSea\Photos\black_and_white"

# Call the function to move photos by color
move_photos_by_color(input_folder, output_folder_red, is_mostly_red, "red")
move_photos_by_color(input_folder, output_folder_blue, is_mostly_blue, "blue")
move_photos_by_color(input_folder, output_folder_green, is_mostly_green, "green")
move_photos_by_color(input_folder, output_folder_bw, is_black_and_white, "black_and_white")
