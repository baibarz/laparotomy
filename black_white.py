import cv2
import os

def convert_to_black_and_white(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Iterate over each file
    for file_name in files:
        # Construct the input and output file paths
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)
        
        try:
            # Read the image
            image = cv2.imread(input_path)
            
            # Check if image is None (could not be read)
            if image is None:
                print(f"Could not read {file_name}. Skipping.")
                continue
            
            # Convert the image to black and white
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Write the black and white image to the output folder
            cv2.imwrite(output_path, gray_image)
            
            print(f"Converted {file_name} to black and white.")
        except Exception as e:
            print(f"Error processing {file_name}: {str(e)}")

# Specify input and output folders
input_folder = r"C:\Users\mmste\Documents\size\raw"
output_folder = r"C:\Users\mmste\Documents\size\bw"

# Call the function to convert images
convert_to_black_and_white(input_folder, output_folder)
