import os
import re

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the mosaic-container and its contents
    # Use a greedy match to find all content between the first <div class="mosaic-container"> and its closing </div>
    container_pattern = re.compile(r'(<div class="mosaic-container">)(.*?)(</div>\s*</div>\s*</section>)', re.DOTALL)
    match = container_pattern.search(content)
    
    if match:
        prefix = match.group(1)
        inner_content = match.group(2)
        suffix = match.group(3)
        
        # Find all images within this section
        # Look for <div class="mosaic-item ...">...<img src="..." alt="...">...</div>
        item_pattern = re.compile(r'<div class="mosaic-item.*?<img src="(.*?)".*?alt="(.*?)".*?</div>', re.DOTALL)
        items = item_pattern.findall(inner_content)
        
        new_items = []
        for i, (src, alt) in enumerate(items):
            extra_class = " m-wide" if i % 4 == 0 else ""
            item_html = f"""
                <div class="mosaic-item{extra_class} wow zoomIn">
                    <a href="{src}">
                        <img src="{src}" alt="{alt}">
                        <div class="gallery-overlay"><i class="fa-solid fa-expand"></i></div>
                    </a>
                </div>"""
            new_items.append(item_html)
        
        new_gallery = f'<div class="mosaic-container gallery-items">{"".join(new_items)}\n            </div>'
        # Replace the entire block
        # We need to be careful with the suffix replacement
        content = container_pattern.sub(new_gallery + '\n        </div>\n    </section>', content)

    # 2. Remove redundant buttons
    button_pattern = re.compile(r'<a href="#" class="btn-premium">.*?</a>\s*<a href="contact.html" class="btn-premium".*?>.*?</a>', re.DOTALL)
    content = button_pattern.sub('', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

project_files = [
    'akshar.html', 'asvattha.html', 'brindavan.html', 'canopus.html', 
    'colossal-terraces.html', 'opera-primus.html', 'spring-leaf.html', 'windsor.html'
]

for filename in project_files:
    if os.path.exists(filename):
        print(f"Processing {filename}...")
        process_html_file(filename)

print("Done.")
