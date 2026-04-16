import os, glob, re

base = os.path.dirname(os.path.abspath(__file__))
# Search in the specified directory
target_dir = r'c:\Users\parth\Downloads\hnm\Rohan 1\Rohan 1\html.awaikenthemes.com\hetch'
files = glob.glob(os.path.join(target_dir, '*.html'))
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()

    # Replace logo inside footer-logo div
    # We look for <div class="footer-logo"> followed by <img ... src="images/logos/logo.jpeg" ...>
    # and replace it with images/logos/logo-footer.png
    
    pattern = r'(<div class="footer-logo">[\s\S]*?<img[^>]*?src=")(images/logos/logo\.(?:jpeg|png|jpg))("[^>]*?>)'
    replacement = r'\1images/logos/logo-footer.png\3'
    
    new_content = re.sub(pattern, replacement, content)

    if new_content != content:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        count += 1

print(f'Updated {count} HTML files.')
