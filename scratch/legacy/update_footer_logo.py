import os, glob, re

base = os.path.dirname(os.path.abspath(__file__))
files = glob.glob(os.path.join(base, '*.html'))
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()

    # Replace logo inside footer-logo div only
    new = re.sub(
        r'(class="footer-logo">\s*<img src=")images/logos/logo\.jpeg(")',
        r'\1images/logos/logo-transparent.png\2',
        content
    )

    if new != content:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new)
        count += 1

print(f'Updated {count} files')
