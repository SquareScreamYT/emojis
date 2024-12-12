from PIL import Image
import os

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def replace_yellow_with_skin_tones(folder_path):
    # Original yellow colors
    yellow1 = hex_to_rgb('#ffd43b')
    yellow2 = hex_to_rgb('#fcc419')
    
    # Skin tones in order
    skin_tones = [
        hex_to_rgb('#fdf0e4'),  # 1
        hex_to_rgb('#f8dcc7'),  # 2
        hex_to_rgb('#f1c7ac'),  # 3
        hex_to_rgb('#e4ad8f'),  # 4
        hex_to_rgb('#cc9477'),  # 5
        hex_to_rgb('#b57a5e'),  # 6
        hex_to_rgb('#9a6548'),  # 7
        hex_to_rgb('#7b4e36'),  # 8
        hex_to_rgb('#5e3b2b'),  # 9
        hex_to_rgb('#3e261a'),  # 10
    ]
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            print(f"Processing: {filename}")
            image_path = os.path.join(folder_path, filename)
            
            # Process 5 tones using pairs of skin tones
            for tone_idx in range(5):
                print(f"  Creating tone {tone_idx + 1}")
                img = Image.open(image_path)
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
                
                data = img.getdata()
                new_data = []
                
                for item in data:
                    if item[:3] == yellow1:
                        new_data.append(skin_tones[tone_idx * 2] + (item[3],))
                    elif item[:3] == yellow2:
                        new_data.append(skin_tones[tone_idx * 2 + 1] + (item[3],))
                    else:
                        new_data.append(item)
                
                img.putdata(new_data)
                
                new_filename = f"{os.path.splitext(filename)[0]}_tone{tone_idx + 1}.png"
                new_path = os.path.join(folder_path, new_filename)
                img.save(new_path, 'PNG')
            print(f"Completed: {filename}\n")

if __name__ == "__main__":
    folder_path = "C:/Users/KFX/OneDrive/Documents/emojis/png/people"
    print("Starting emoji skin tone conversion...")
    replace_yellow_with_skin_tones(folder_path)
    print("All files processed successfully!")
