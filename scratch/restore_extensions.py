import os
import re

def restore_extensions(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Target common internal links that don't have extensions
                    # Skip mailto, tel, http, and already extended links
                    def replacer(match):
                        link = match.group(1)
                        if link == "./" or link == "/":
                            return 'href="index.html"'
                        if "." not in link and not link.startswith(("#", "mailto", "tel", "http")):
                            return f'href="{link}.html"'
                        return match.group(0)

                    content = re.sub(r'href="([^"]+)"', replacer, content)
                    
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                except:
                    pass

if __name__ == "__main__":
    restore_extensions(".")
