import os

page_titles = {
    "index.html": "Opera Homes | Excellence in Urban Landscape",
    "about.html": "About Us | Opera Homes",
    "awards.html": "Awards & Recognitions | Opera Homes",
    "projects.html": "Project Gallery | Opera Homes",
    "residential.html": "Residential Projects | Opera Homes",
    "commercial.html": "Commercial Projects | Opera Homes",
    "contact.html": "Contact Us | Opera Homes",
    "404.html": "404 Page Not Found | Opera Homes",
    "akshar.html": "Opera Akshar | Project Details",
    "asvattha.html": "Opera Asvattha | Future Residential Vision",
    "autumn-garden.html": "Opera Autumn Garden | Luxury Living",
    "brindavan.html": "Opera Brindavan | Modern Community Living",
    "canopus.html": "Opera Canopus | Certified Urban Excellence",
    "colossal-terraces.html": "Colossal Terraces | Commercial Excellence",
    "opera-primus.html": "Opera Primus | Luxury Residential Showcase",
    "spring-leaf.html": "Opera Spring Leaf | Modern Residential Serenity",
    "tranquil-earth.html": "Opera Tranquil Earth | Modern Residential Sanctuary",
    "windsor.html": "Opera Windsor | Luxurious Residential Grandeur"
}

def update_exact_titles(directory):
    for filename, title in page_titles.items():
        path = os.path.join(directory, filename)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            import re
            content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated title for {filename}")

if __name__ == "__main__":
    update_exact_titles(".")
