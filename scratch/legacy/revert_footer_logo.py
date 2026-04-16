import os, glob, re

base = os.path.dirname(os.path.abspath(__file__))
files = glob.glob(os.path.join(base, '*.html'))
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()

    new = re.sub(
        r'(class="footer-logo">\s*<img src=")images/logos/logo-transparent\.png(")',
        r'\1images/logos/logo.jpeg\2',
        content
    )

    if new != content:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new)
        count += 1

print(f'Reverted {count} files to logo.jpeg')
