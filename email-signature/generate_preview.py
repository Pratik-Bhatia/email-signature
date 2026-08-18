import os
import base64
import re

def main():
    signature_path = r'email-signature\signature.html'
    preview_path = r'email-signature\preview.html'
    assets_dir = r'email-signature\assets'
    
    with open(signature_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    wrapper = """<!DOCTYPE html>
<html>
<head>
    <title>Signature Preview</title>
    <style>
        body { font-family: sans-serif; background-color: #f0f0f0; padding: 40px; display: flex; flex-direction: column; align-items: center; }
        .email-container { background: white; width: 100%; max-width: 1100px; padding: 40px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        .info { max-width: 1100px; width: 100%; text-align: left; margin-bottom: 20px; color: #666; }
    </style>
</head>
<body>
    <div class="info">
        <h3>Officeneed Signature Preview</h3>
        <p>Below is how your signature will appear in emails. The layout is optimized for desktops up to 1000px wide, matching the visual scale requested.</p>
    </div>
    <div class="email-container">
        <!-- Copied signature with local asset paths for preview purposes -->
"""
    table_match = re.search(r'<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 1060px;.*?>.*</table>', html, re.DOTALL)
    if table_match:
        sig_html = table_match.group(0)
    else:
        sig_html = html
        
    def replace_with_b64(match):
        filename = match.group(1).split('/')[-1]
        filepath = os.path.join(assets_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as img_f:
                b64_data = base64.b64encode(img_f.read()).decode('utf-8')
            full_match = match.group(0)
            if 'src=' in full_match:
                return f'src="data:image/png;base64,{b64_data}"'
            elif 'background=' in full_match:
                return f'background="data:image/png;base64,{b64_data}"'
            elif 'url(' in full_match:
                return f"url('data:image/png;base64,{b64_data}')"
        return match.group(0)

    sig_html = re.sub(r'src="(https://www.officeneed.in/email-signature/assets/[^"]+)"', replace_with_b64, sig_html)
    sig_html = re.sub(r'background="(https://www.officeneed.in/email-signature/assets/[^"]+)"', replace_with_b64, sig_html)
    sig_html = re.sub(r"url\('(https://www.officeneed.in/email-signature/assets/[^']+)'\)", replace_with_b64, sig_html)
    
    final_html = wrapper + sig_html + "\n    </div>\n</body>\n</html>"
    
    with open(preview_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
        
    print("Preview generated and Base64 embedded successfully.")

if __name__ == '__main__':
    main()
