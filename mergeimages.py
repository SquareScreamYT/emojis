from PIL import Image
import os

def merge_images(image1_path, image2_path, output_path):
    print(f"Merging: {os.path.basename(image1_path)} + {os.path.basename(image2_path)}")
    
    # Open both images
    base = Image.open(image1_path)
    overlay = Image.open(image2_path)
    
    # Convert both to RGBA if they aren't already
    if base.mode != 'RGBA':
        base = base.convert('RGBA')
    if overlay.mode != 'RGBA':
        overlay = overlay.convert('RGBA')
    
    # Create new merged image
    merged = Image.alpha_composite(base, overlay)
    
    # Save merged image
    merged.save(output_path, 'PNG')
    print(f"Created: {os.path.basename(output_path)}")

if __name__ == "__main__":
    image1 = "C:/Users/KFX/OneDrive/Documents/emojis/png/people/image1.png"
    image2 = "C:/Users/KFX/OneDrive/Documents/emojis/png/people/image2.png"
    result = "C:/Users/KFX/OneDrive/Documents/emojis/png/people/merged.png"
    
    print("Starting image merge...")
    merge_images(image1, image2, result)
    print("Merge completed!")
