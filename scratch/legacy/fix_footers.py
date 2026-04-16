import os, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROPER_FOOTER = '''    <!-- Footer Start -->
    <footer class="main-footer">
        <div class="container">
            <div class="row">
                <div class="col-lg-4 col-md-6">
                    <div class="about-footer">
                        <div class="footer-logo">
                            <img src="images/logos/logo.jpeg" alt="Opera Homes">
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

# Project detail pages with broken/minimal footers
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

# Pattern to match any existing footer block (from <footer to </footer>)
FOOTER_PATTERN = re.compile(r'\s*<!-- (?:Footer|Floating Action Bar).*?-->\s*<footer[\s\S]*?</footer>', re.IGNORECASE)
# Also match standalone floating action bar divs
ACTION_BAR_PATTERN = re.compile(r'\s*<!-- Floating Action Bar -->\s*<div class="floating-action-bar[\s\S]*?</div>\s*', re.IGNORECASE)

count = 0
for filename in TARGET_FILES:
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"SKIP (not found): {filename}")
        continue

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Remove any floating action bar divs first
    content = ACTION_BAR_PATTERN.sub('\n', content)

    # Replace existing footer with proper one
    new_content = FOOTER_PATTERN.sub('\n\n' + PROPER_FOOTER, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filename}")
        count += 1
    else:
        print(f"No footer match: {filename}")

print(f"\nDone! Updated {count} files.")
