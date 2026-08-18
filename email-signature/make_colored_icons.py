import os
import urllib.request
from PIL import Image, ImageDraw

def download_image(url, save_path):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(save_path, 'wb') as out_file:
        out_file.write(response.read())

def make_high_res_colored_icon(raw_path, final_name, bg_color='#FFD700', padding_factor=0.6):
    final_path = os.path.join('email-signature', 'assets', final_name)
    try:
        icon = Image.open(raw_path).convert("RGBA")
    except Exception as e:
        print(f"Failed to open {raw_path}: {e}")
        return
        
    size = (128, 128)
    img = Image.new('RGBA', size, (255, 255, 255, 0))
    
    # Draw an anti-aliased yellow circle
    large_size = (512, 512)
    circle_img = Image.new('RGBA', large_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(circle_img)
    draw.ellipse((0, 0, 511, 511), fill=bg_color)
    circle_img = circle_img.resize(size, Image.Resampling.LANCZOS)
    
    img.paste(circle_img, (0, 0), circle_img)
    
    # Calculate icon size
    # Icons8 icons are usually square. 
    icon_w, icon_h = icon.size
    
    # We want to crop out the empty padding that Icons8 might have.
    # Actually, we can just find the bounding box of non-transparent pixels.
    bbox = icon.getbbox()
    if bbox:
        icon = icon.crop(bbox)
        icon_w, icon_h = icon.size
        
    target_icon_size = int(128 * padding_factor)
    
    if icon_w > icon_h:
        new_w = target_icon_size
        new_h = int(icon_h * (target_icon_size / icon_w))
    else:
        new_h = target_icon_size
        new_w = int(icon_w * (target_icon_size / icon_h))
        
    if final_name == 'youtube.png':
        new_w = int(128 * 0.65)
        new_h = int(icon_h * (new_w / icon_w))
        
    icon = icon.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    offset_x = (size[0] - new_w) // 2
    offset_y = (size[1] - new_h) // 2
    img.alpha_composite(icon, (offset_x, offset_y))
    
    img.save(final_path, format='PNG', optimize=True)
    print(f"Generated {final_name}")

urls = {
    'linkedin-colored.png': 'https://img.icons8.com/color/512/linkedin.png',
    'instagram-colored.png': 'https://img.icons8.com/color/512/instagram-new.png',
    'facebook-colored.png': 'https://img.icons8.com/color/512/facebook-new.png',
    'youtube-colored.png': 'https://img.icons8.com/color/512/youtube-play.png'
}

for raw_name, url in urls.items():
    raw_path = os.path.join('email-signature', 'assets', raw_name)
    try:
        download_image(url, raw_path)
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        continue
        
    final_name = raw_name.replace('-colored', '')
    make_high_res_colored_icon(raw_path, final_name)
