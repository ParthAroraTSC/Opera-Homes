import os
import re

def final_cleanup(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".html", ".js", ".css")):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Remove HTTrack Mirror comments
                    content = re.sub(r'<!-- Mirrored from [^>]* -->', '', content)
                    # Remove any remaining "Hetch" in text
                    content = content.replace('Hetch', 'Opera Homes')
                    content = content.replace('hetch', 'opera-homes') # for generic text, not paths
                    
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                except:
                    pass

if __name__ == "__main__":
    final_cleanup(".")
