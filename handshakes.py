from PIL import Image
import os

def merge_handshakes(src_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all left handshake variations
    left_hands = [f for f in os.listdir(src_folder) if f.startswith('handshake_left_tone')]
    right_hands = [f for f in os.listdir(src_folder) if f.startswith('handshake_right_tone')]
    
    # Create all possible combinations
    for left in left_hands:
        for right in right_hands:
            print(f"Creating combination: {left} + {right}")
            
            # Open images
            left_img = Image.open(os.path.join(src_folder, left))
            right_img = Image.open(os.path.join(src_folder, right))
            
            # Convert to RGBA
            if left_img.mode != 'RGBA':
                left_img = left_img.convert('RGBA')
            if right_img.mode != 'RGBA':
                right_img = right_img.convert('RGBA')
            
            # Merge images
            merged = Image.alpha_composite(left_img, right_img)
            
            # Create output filename (e.g., handshake_tone1-tone2.png)
            left_tone = left.split('_tone')[1].split('.')[0]
            right_tone = right.split('_tone')[1].split('.')[0]
            output_name = f"handshake_tone{left_tone}-tone{right_tone}.png"
            
            # Save merged image
            output_path = os.path.join(output_folder, output_name)
            merged.save(output_path, 'PNG')
            print(f"Created: {output_name}")

if __name__ == "__main__":
    src_folder = "C:/Users/KFX/OneDrive/Documents/emojis/png/people_1color"
    output_folder = "C:/Users/KFX/OneDrive/Documents/emojis/png/handshakes"
    print("Starting handshake combinations...")
    merge_handshakes(src_folder, output_folder)
    print("All handshake combinations completed!")
