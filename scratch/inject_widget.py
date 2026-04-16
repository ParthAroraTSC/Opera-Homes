import os
import re
import sys

# Standardize path handling
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
from core.html_processor import HTMLProcessor

# ==========================================
# CONFIGURATION & ORIGINAL DATA PRESERVATION
# ==========================================
# --- ORIGINAL CODE START --- 
CSS_LINK = '    <!-- Floating Contact Widget Css -->\n\t<link href="assets/css/floating-contact.css" rel="stylesheet">\n'

WIDGET_HTML = '''
    <!-- Floating Contact Widget Start -->
    <div class="floating-contact-wrapper" id="floatingContact">
        <div class="contact-options">
            <a href="tel:+918041230476" class="contact-option phone" title="Call Us">
                <i class="fa-solid fa-phone"></i>
            </a>
            <a href="https://wa.me/919740213520" target="_blank" class="contact-option whatsapp" title="WhatsApp Us">
                <i class="fa-brands fa-whatsapp"></i>
            </a>
        </div>
        <div class="contact-trigger" onclick="document.getElementById('floatingContact').classList.toggle('active')">
            <div class="trigger-icon">
                <i class="fa-solid fa-comment-dots"></i>
                <i class="fa-solid fa-xmark"></i>
            </div>
        </div>
    </div>
    <!-- Floating Contact Widget End -->
'''
# --- ORIGINAL CODE END --- 

def main():
    # Base directory is the root where HTML files are
    root_dir = os.path.dirname(current_dir)
    processor = HTMLProcessor(base_dir=root_dir)
    files = processor.get_html_files()
    count = 0

    for filename in files:
        content = processor.read_file(filename)
        changed = False

        # Add CSS link before </head> if not exists
        if 'floating-contact.css' not in content and '</head>' in content:
            content = content.replace('</head>', CSS_LINK + '</head>', 1)
            changed = True

        # Add widget HTML before </body> if not exists
        if 'floating-contact-wrapper' not in content and '</body>' in content:
            content = content.replace('</body>', WIDGET_HTML + '</body>', 1)
            changed = True

        if changed:
            processor.write_file(filename, content)
            count += 1
            print(f"Updated: {filename}")

    print(f"\nDone! Updated {count} files.")

if __name__ == "__main__":
    main()
