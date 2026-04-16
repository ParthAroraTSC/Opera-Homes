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
PROPER_FOOTER = '''    <!-- Footer Start -->
    <footer class="main-footer">
        <div class="container">
            <div class="row">
                <div class="col-lg-4 col-md-6">
                    <div class="about-footer">
                        <div class="footer-logo">
                            <img src="assets/images/logos/logo-footer.png" alt="Opera Homes">
                        </div>
                        <div class="about-footer-content">
                            <p>Opera Homes with over 15 years of Experience in shaping the emerging urban landscape., has elevated itself of creating some of the landmark residential and commercial projects in bangalore.</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6">
                    <div class="footer-links">
                        <h3>Follow Links</h3>
                        <ul>
                            <li><a href="about.html">About us</a></li>
                            <li><a href="residential.html">Residential</a></li>
                            <li><a href="commercial.html">Commercial</a></li>
                            <li><a href="projects.html">Gallery</a></li>
                            <li><a href="contact.html">Contact Us</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6">
                    <div class="footer-links">
                        <h3>Social Links</h3>
                        <div class="footer-social-links">
                            <ul>
                                <li><a href="#"><i class="fa-brands fa-facebook-f"></i></a></li>
                                <li><a href="#"><i class="fa-brands fa-instagram"></i></a></li>
                                <li><a href="#"><i class="fa-brands fa-youtube"></i></a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="footer-contact-box footer-links">
                        <h3>Contact Details</h3>
                        <div class="footer-contact-item">
                            <div class="icon-box"><i class="fa-solid fa-phone" style="color:#64748b;"></i></div>
                            <div class="footer-contact-content"><p>+91 8041230476</p></div>
                        </div>
                        <div class="footer-contact-item">
                            <div class="icon-box"><i class="fa-solid fa-phone" style="color:#64748b;"></i></div>
                            <div class="footer-contact-content"><p>+91 9740213520</p></div>
                        </div>
                        <div class="footer-contact-item">
                            <div class="icon-box"><i class="fa-solid fa-envelope" style="color:#64748b;"></i></div>
                            <div class="footer-contact-content"><p>info.sales@operahomes.in</p></div>
                        </div>
                        <div class="footer-contact-item">
                            <div class="icon-box"><i class="fa-solid fa-location-dot" style="color:#64748b;"></i></div>
                            <div class="footer-contact-content"><p>No. 149 - 3rd Floor - Above KFC Restaurant Jayanagar 4th Block, Bangalore - 560011</p></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="footer-copyright">
                <div class="row align-items-center">
                    <div class="col-lg-12">
                        <div class="footer-copyright-text">
                            <p>Copyright &copy; 2024 All Rights Reserved.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    <!-- Footer End -->'''

TARGET_FILES = [
    'opera-primus.html',
    'brindavan.html',
    'canopus.html',
    'colossal-terraces.html',
    'autumn-garden.html',
    'spring-leaf.html',
    'tranquil-earth.html',
    'windsor.html',
    'akshar.html',
    'asvattha.html',
]

FOOTER_PATTERN = re.compile(r'\s*<!-- (?:Footer|Floating Action Bar).*?-->\s*<footer[\s\S]*?</footer>', re.IGNORECASE)
ACTION_BAR_PATTERN = re.compile(r'\s*<!-- Floating Action Bar -->\s*<div class="floating-action-bar[\s\S]*?</div>\s*', re.IGNORECASE)
# --- ORIGINAL CODE END --- 

def main():
    # Assets are now in the parent directory's 'assets' folder
    # However, the processing still happens on the HTML files in the parent root
    processor = HTMLProcessor(base_dir=os.path.dirname(current_dir))
    
    tasks = [
        {'pattern': ACTION_BAR_PATTERN, 'replacement': '\n', 'name': 'Cleanup Action Bar'},
        {'pattern': FOOTER_PATTERN, 'replacement': '\n\n' + PROPER_FOOTER, 'name': 'Update Footer'}
    ]
    
    processor.process_batch(tasks, target_files=processor.get_html_files())

if __name__ == "__main__":
    main()
