import os
import base64
import re

def main():
    preview_path = r'email-signature\preview.html'
    assets_dir = r'email-signature\assets'
    
    with open(preview_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    def replace_src(match):
        filename = match.group(1)
        filepath = os.path.join(assets_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as img_f:
                b64_data = base64.b64encode(img_f.read()).decode('utf-8')
            return f'src="data:image/png;base64,{b64_data}"'
        return match.group(0)

    def replace_bg(match):
        filename = match.group(1)
        filepath = os.path.join(assets_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as img_f:
                b64_data = base64.b64encode(img_f.read()).decode('utf-8')
            return f'background="data:image/png;base64,{b64_data}"'
        return match.group(0)
        
    def replace_url(match):
        filename = match.group(1)
        filepath = os.path.join(assets_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as img_f:
                b64_data = base64.b64encode(img_f.read()).decode('utf-8')
            return f"url('data:image/png;base64,{b64_data}')"
        return match.group(0)

    # First, let's fix the broken ones if they exist
    # If the file already has `src="assets/data:image...` we need to un-break it.
    # The best way is to regenerate preview.html from scratch.
    pass

if __name__ == '__main__':
    main()
