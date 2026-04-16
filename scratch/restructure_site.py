import os
import re

def restructure_site(root_dir):
    pages_dir = os.path.join(root_dir, "pages")
    if not os.path.exists(pages_dir):
        os.makedirs(pages_dir)
    
    html_files = [f for f in os.listdir(root_dir) if f.endswith(".html") and f != "index.html"]
    
    # 1. Update index.html links
    index_path = os.path.join(root_dir, "index.html")
    if os.path.exists(index_path):
        print("Updating index.html...")
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Change href="about.html" to href="pages/about.html"
        for hf in html_files:
            content = content.replace(f'href="{hf}"', f'href="pages/{hf}"')
            
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)

    # 2. Process and Move other HTML files
    for hf in html_files:
        old_path = os.path.join(root_dir, hf)
        new_path = os.path.join(pages_dir, hf)
        
        print(f"Processing and moving {hf}...")
        with open(old_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update asset paths from ./ to ../
        content = re.sub(r'href="assets/', 'href="../assets/', content)
        content = re.sub(r'src="assets/', 'src="../assets/', content)
        # Update links to index.html
        content = content.replace('href="index.html"', 'href="../index.html"')
        # Update links to other sibling pages (already in /pages)
        # No change needed if they are in the same folder, BUT links might have been absolute-ish
        
        with open(old_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        # Move it
        if os.path.exists(new_path):
            os.remove(new_path)
        os.rename(old_path, new_path)

if __name__ == "__main__":
    restructure_site(".")
