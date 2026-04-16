import os
import re

# Refactored paths mapping
path_mapping = {
    'css/': 'assets/css/',
    'js/': 'assets/js/',
    'images/': 'assets/images/',
    'webfonts/': 'assets/webfonts/',
    'pdf/': 'assets/pdf/',
}

def update_paths(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Original lines preservation is key
    # We are only updating the attribute values
    
    for old_path, new_path in path_mapping.items():
        # Match src="css/...", href="css/...", etc.
        pattern = r'(src|href|url)\s*=\s*(["\'])\s*' + re.escape(old_path)
        replacement = r'\1=\2' + new_path
        content = re.sub(pattern, replacement, content)
        
        # Match url('../images/...') in CSS-like blocks inside HTML
        pattern_css = r'url\(\s*(["\']?)\s*' + re.escape(old_path)
        replacement_css = r'url(\1' + new_path
        content = re.sub(pattern_css, replacement_css, content)

    # Specific update for the new main.js
    content = content.replace('assets/js/function.js', 'assets/js/main.js')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    root_dir = '.'
    for filename in os.listdir(root_dir):
        if filename.endswith('.html'):
            print(f"Updating {filename}...")
            update_paths(os.path.join(root_dir, filename))

if __name__ == "__main__":
    main()
