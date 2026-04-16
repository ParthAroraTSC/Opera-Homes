import os
import re

def update_favicon(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace the classic favicon link if exists, or add it
                new_favicon = '<link rel="icon" type="image/jpeg" href="assets/images/logos/logo.jpeg">\n\t<link rel="apple-touch-icon" href="assets/images/logos/logo.jpeg">'
                
                if '<link rel="shortcut icon"' in content:
                    content = re.sub(r'<link rel="shortcut icon"[^>]*>', new_favicon, content)
                    print(f"Updated favicon in {file}")
                elif '</head>' in content:
                    content = content.replace('</head>', f'\t{new_favicon}\n</head>')
                    print(f"Added favicon in {file}")
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == "__main__":
    update_favicon(".")
