from PIL import Image

def divide_photo_into_strips(image_path, strip_width_cm, output_folder):
    # Open the image
    img = Image.open(image_path)

    # Calculate the pixel width of each strip
    pixels_per_cm = img.width / (img.width / strip_width_cm)  # Calculate pixels per cm for the image
    strip_width_pixels = int(strip_width_cm * pixels_per_cm)
    
    # Calculate the number of strips
    num_strips = img.width // strip_width_pixels
    
    # Create and save each strip
    for i in range(num_strips):
        left = i * strip_width_pixels
        right = (i + 1) * strip_width_pixels
        
        # Crop the image
        strip = img.crop((left, 0, right, img.height))
        
        # Save the strip to the output folder
        strip.save(f"{output_folder}/strip_{i+1}.png")

# Example usage
image_path = "x/77.png"  # Replace with the path to your image
strip_width_cm = 16
output_folder = "strips/"  # Create this folder in advance

divide_photo_into_strips(image_path, strip_width_cm, output_folder)
