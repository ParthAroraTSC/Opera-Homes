import os
import re
import sys

# Standardize path handling
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
from core.html_processor import HTMLProcessor

def cleanup():
    root_dir = os.path.dirname(current_dir)
    processor = HTMLProcessor(base_dir=root_dir)
    
    # 1. Cleanup Index Styles
    index_style_pattern = re.compile(r'<style>\s*\.about-premium-akshar[\s\S]*?</style>')
    index_link = '    <!-- Akshar Section Component Css -->\n\t<link href="assets/css/components/akshar-section.css" rel="stylesheet">\n'
    
    # 2. Cleanup Project Detail Styles
    project_style_pattern = re.compile(r'<style>\s*:root\s*{\s*--dark-blue:[\s\S]*?</style>')
    project_link = '    <!-- Project Detail Page Css -->\n\t<link href="assets/css/pages/project-details.css" rel="stylesheet">\n'
    
    # 3. Cleanup Contact Styles
    contact_style_pattern = re.compile(r'<style>\s\* ── Contact Page[\s\S]*?</style>')
    contact_link = '    <!-- Contact Page Css -->\n\t<link href="assets/css/pages/contact.css" rel="stylesheet">\n'

    files = processor.get_html_files()
    count = 0

    for filename in files:
        content = processor.read_file(filename)
        original = content
        
        # Check and apply index cleanup
        if index_style_pattern.search(content):
            content = index_style_pattern.sub('', content)
            if 'akshar-section.css' not in content:
                content = content.replace('</head>', index_link + '</head>')
        
        # Check and apply project cleanup
        if project_style_pattern.search(content):
            content = project_style_pattern.sub('', content)
            if 'project-details.css' not in content:
                content = content.replace('</head>', project_link + '</head>')

        # Check and apply contact cleanup
        if contact_style_pattern.search(content):
            content = contact_style_pattern.sub('', content)
            if 'contact.css' not in content:
                content = content.replace('</head>', contact_link + '</head>')

        if content != original:
            processor.write_file(filename, content)
            count += 1
            print(f"Cleaned up styles in: {filename}")

    print(f"\nDone! Cleaned up {count} files.")

if __name__ == "__main__":
    cleanup()
