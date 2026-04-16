import os
import re

def clean_urls(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Replace href="page.html" with href="page"
                    # But only for internal links
                    def replacer(match):
                        link = match.group(1)
                        if link == "index.html":
                            return 'href="./"'
                        if not link.startswith(("http", "#", "mailto", "tel")):
                            return f'href="{link.replace(".html", "")}"'
                        return match.group(0)

                    content = re.sub(r'href="([^"]+\.html)"', replacer, content)
                    
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                except:
                    pass

if __name__ == "__main__":
    clean_urls(".")
