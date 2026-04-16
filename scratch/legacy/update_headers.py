import os
import re

header_pattern = re.compile(r'<!-- Topbar Section Start -->.*?<!-- Header End -->', re.DOTALL)
# Alternative pattern if the comment is missing but the class is there
alt_pattern = re.compile(r'<div class="topbar">.*?<!-- Header End -->', re.DOTALL)
# Third pattern for files using Header Start
third_pattern = re.compile(r'<!-- Header Start -->.*?<!-- Header End -->', re.DOTALL)

new_header = """    <!-- Header Start -->
	<header class="main-header">
		<div class="header-sticky">
			<nav class="navbar navbar-expand-lg">
				<div class="container">
					<!-- Logo Start -->
					<a class="navbar-brand" href="index.html">
						<div class="logo-white-box">
						    <img src="images/logos/logo.jpeg" alt="Opera Homes">
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

files_updated = 0

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try primary pattern
        if header_pattern.search(content):
            updated_content = header_pattern.sub(new_header, content)
            files_updated += 1
        # Try alternate pattern
        elif alt_pattern.search(content):
            updated_content = alt_pattern.sub(new_header, content)
            files_updated += 1
        # Try third pattern
        elif third_pattern.search(content):
            updated_content = third_pattern.sub(new_header, content)
            files_updated += 1
        else:
            print(f"Skipping {filename} - header pattern not found")
            continue
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)

print(f"Successfully updated {files_updated} files.")
