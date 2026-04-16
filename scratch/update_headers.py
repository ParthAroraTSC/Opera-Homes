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
header_pattern = re.compile(r'<!-- Topbar Section Start -->.*?<!-- Header End -->', re.DOTALL)
alt_pattern = re.compile(r'<div class="topbar">.*?<!-- Header End -->', re.DOTALL)
third_pattern = re.compile(r'<!-- Header Start -->.*?<!-- Header End -->', re.DOTALL)

# NOTE: Updated image paths to 'assets/images/...' to match improved structure
new_header = """    <!-- Header Start -->
	<header class="main-header">
		<div class="header-sticky">
			<nav class="navbar navbar-expand-lg">
				<div class="container">
					<!-- Logo Start -->
					<a class="navbar-brand" href="index.html">
						<div class="logo-white-box">
						    <img src="assets/images/logos/logo.jpeg" alt="Opera Homes">
						</div>
					</a>
					<!-- Logo End -->

					<!-- Main Menu Start -->
					<div class="collapse navbar-collapse main-menu">
                        <div class="nav-menu-wrapper">
                            <ul class="navbar-nav mr-auto" id="menu">
                                <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>                                
                                <li class="nav-item"><a class="nav-link" href="about.html">About Us</a></li>
                                <li class="nav-item submenu"><a class="nav-link" href="#">Our Projects</a>
                                    <ul>                                        
                                        <li class="nav-item"><a class="nav-link" href="residential.html">Residential</a></li>
                                        <li class="nav-item"><a class="nav-link" href="commercial.html">Commercial</a></li>
                                    </ul>
                                </li>
                                <li class="nav-item"><a class="nav-link" href="awards.html">Awards</a></li>
                                <li class="nav-item"><a class="nav-link" href="projects.html">Gallery</a></li>
                                <li class="nav-item"><a class="nav-link" href="contact.html">Contact Us</a></li>                             
                            </ul>
                        </div>
                        <!-- Header Social Icons Start -->
                        <div class="header-social-icons">
                            <ul>
                                <li><a href="#"><i class="fa-brands fa-facebook-f"></i></a></li>
                                <li><a href="#"><i class="fa-brands fa-instagram"></i></a></li>
                                <li><a href="#"><i class="fa-brands fa-youtube"></i></a></li>
                            </ul>
                        </div>
                        <!-- Header Social Icons End -->
					</div>
					<!-- Main Menu End -->
					<div class="navbar-toggle"></div>
				</div>
			</nav>
			<div class="responsive-menu"></div>
		</div>
	</header>
	<!-- Header End -->"""
# --- ORIGINAL CODE END --- 

def main():
    root_dir = os.path.dirname(current_dir)
    processor = HTMLProcessor(base_dir=root_dir)
    
    files = processor.get_html_files()
    count = 0
    
    for filename in files:
        content = processor.read_file(filename)
        updated_content = None
        
        if header_pattern.search(content):
            updated_content = header_pattern.sub(new_header, content)
        elif alt_pattern.search(content):
            updated_content = alt_pattern.sub(new_header, content)
        elif third_pattern.search(content):
            updated_content = third_pattern.sub(new_header, content)
            
        if updated_content and updated_content != content:
            processor.write_file(filename, updated_content)
            count += 1
            
    print(f"Successfully updated {count} files.")

if __name__ == "__main__":
    main()
