import os
import re

def update_titles(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace Hetch with Opera Homes in titles
                if 'Hetch - Windows and Doors HTML Template' in content:
                    content = content.replace('Hetch - Windows and Doors HTML Template', 'Opera Homes | Excellence in Urban Landscape')
                    print(f"Updated title in {file}")
                
                content = content.replace('Hetch', 'Opera Homes')
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == "__main__":
    update_titles(".")
