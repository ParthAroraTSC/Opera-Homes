import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSS_LINK = '    <!-- Floating Contact Widget Css -->\n\t<link href="css/floating-contact.css" rel="stylesheet">\n'

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

html_files = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]
count = 0

for filename in html_files:
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    changed = False

    # Add CSS link before </head>
    if 'floating-contact.css' not in content and '</head>' in content:
        content = content.replace('</head>', CSS_LINK + '</head>', 1)
        changed = True

    # Add widget HTML before </body>
    if 'floating-contact-wrapper' not in content and '</body>' in content:
        content = content.replace('</body>', WIDGET_HTML + '</body>', 1)
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filename}")
        count += 1
    else:
        print(f"Skipped (already done): {filename}")

print(f"\nDone! Updated {count} files.")
