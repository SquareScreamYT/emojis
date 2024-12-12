from PIL import Image
import os

def make_transparent(folder_path):
    # Ensure folder path exists
    if not os.path.exists(folder_path):
        return "Folder not found"
    
    # Get all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Open image
            image_path = os.path.join(folder_path, filename)
            img = Image.open(image_path)
            
            # Convert image to RGBA if it isn't already
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Get image data
            data = img.getdata()
            
            # Create new data with transparent pixels
            new_data = []
            for item in data:
                # If pixel is white (or near white), make it transparent
                if item[0] >= 250 and item[1] >= 250 and item[2] >= 250:
                    new_data.append((255, 255, 255, 0))
                else:
                    new_data.append(item)
            
            # Update image with new data
            img.putdata(new_data)
            
            # Save the modified image, overwriting the original
            img.save(image_path, 'PNG')
            
    return "Processing complete!"

# Example usage
if __name__ == "__main__":
    folder_path = "C:/Users/KFX/OneDrive/Documents/emojis/png/people"
    make_transparent(folder_path)
