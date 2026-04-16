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
# Replace logo inside footer-logo div only
LOGO_PATTERN = re.compile(r'(class="footer-logo">\s*<img src=")images/logos/logo\.jpeg(")')
REPLACEMENT = r'\1images/logos/logo-transparent.png\2'
# --- ORIGINAL CODE END --- 

def main():
    processor = HTMLProcessor(base_dir=os.path.dirname(current_dir))
    
    tasks = [
        {
            'name': 'Update Footer Logo',
            'pattern': LOGO_PATTERN,
            'replacement': REPLACEMENT
        }
    ]
    
    processor.process_batch(tasks)

if __name__ == "__main__":
    main()
