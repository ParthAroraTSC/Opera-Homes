import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the about section using regex
pattern = re.compile(
    r'<!-- About Us Section Start -->.*?<!-- About Us Section End -->',
    re.DOTALL
)

new_section = '''<!-- About Us Section Start -->
    <style>
        .about-premium-akshar { padding: 100px 0; background: #f8fafc; }
        .akshar-img-grid { display:grid; grid-template-columns:1.4fr 1fr; gap:16px; height:520px; }
        .akshar-img-main { position:relative; border-radius:16px; overflow:hidden; }
        .akshar-img-main img { width:100%; height:100%; object-fit:cover; }
        .akshar-img-badge { position:absolute; bottom:20px; left:20px; background:#14183e; color:#fff; padding:10px 18px; border-radius:10px; text-align:center; }
        .akshar-img-badge .badge-num { display:block; font-size:13px; font-weight:800; color:#3b82f6; letter-spacing:2px; }
        .akshar-img-badge .badge-txt { font-size:12px; color:#94a3b8; }
        .akshar-img-side { display:flex; flex-direction:column; gap:16px; }
        .akshar-img-top, .akshar-img-bottom { flex:1; border-radius:16px; overflow:hidden; }
        .akshar-img-top img, .akshar-img-bottom img { width:100%; height:100%; object-fit:cover; }
        .akshar-content-new { padding-left:20px; }
        .akshar-tag { display:inline-block; background:#eff6ff; color:#3b82f6; font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:2px; padding:6px 16px; border-radius:20px; margin-bottom:20px; }
        .akshar-content-new h2 { font-size:52px; font-weight:800; color:#14183e; line-height:1.1; margin-bottom:24px; }
        .akshar-content-new h2 em { font-style:normal; color:#3b82f6; }
        .akshar-quote { border-left:4px solid #3b82f6; padding-left:20px; margin-bottom:20px; }
        .akshar-quote p { font-size:17px; color:#475569; font-style:italic; line-height:1.7; margin:0; }
        .akshar-desc { font-size:16px; color:#64748b; line-height:1.8; margin-bottom:28px; }
        .akshar-highlights { margin-bottom:35px; }
        .akshar-hl-item { display:flex; align-items:flex-start; gap:12px; margin-bottom:12px; font-size:15px; color:#334155; }
        .akshar-hl-item i { color:#3b82f6; margin-top:2px; flex-shrink:0; }
        .akshar-btns { display:flex; gap:14px; flex-wrap:wrap; }
        .btn-akshar-primary { background:#14183e; color:#fff; padding:14px 32px; border-radius:8px; font-weight:700; font-size:14px; text-transform:uppercase; letter-spacing:1px; text-decoration:none; transition:0.3s; }
        .btn-akshar-primary:hover { background:#3b82f6; color:#fff; }
        .btn-akshar-outline { background:transparent; color:#14183e; padding:14px 32px; border-radius:8px; font-weight:700; font-size:14px; text-transform:uppercase; letter-spacing:1px; text-decoration:none; border:2px solid #14183e; transition:0.3s; }
        .btn-akshar-outline:hover { background:#14183e; color:#fff; }
        @media (max-width:991px) {
            .akshar-img-grid { height:380px; }
            .akshar-content-new { padding-left:0; margin-top:30px; }
            .akshar-content-new h2 { font-size:38px; }
        }
        @media (max-width:576px) {
            .akshar-img-grid { grid-template-columns:1fr; height:auto; }
            .akshar-img-side { flex-direction:row; height:180px; }
        }
    </style>

    <div class="about-premium about-premium-akshar">
        <div class="container">
            <div class="row align-items-center g-5">
                <div class="col-lg-6">
                    <div class="akshar-img-grid wow fadeInLeft">
                        <div class="akshar-img-main">
                            <img src="images/about/WhatsApp-Image-2025-12-26-at-11.26.48-AM.png" alt="Opera Akshar">
                            <div class="akshar-img-badge">
                                <span class="badge-num">RERA</span>
                                <span class="badge-txt">Approved</span>
                            </div>
                        </div>
                        <div class="akshar-img-side">
                            <div class="akshar-img-top"><img src="images/hero/View4Dusk.jpg" alt=""></div>
                            <div class="akshar-img-bottom"><img src="images/hero/View1Dusk.jpg" alt=""></div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="akshar-content-new wow fadeInRight">
                        <span class="akshar-tag">Ongoing Project &middot; Jayanagar 3rd Block</span>
                        <h2>Welcome To<br><em>Opera Akshar</em></h2>
                        <div class="akshar-quote">
                            <p>"Your home tells the story of your life. It is an ode to all your achievements. It represents every milestone you've crossed."</p>
                        </div>
                        <p class="akshar-desc">That's why we've created Opera Akshar for you — not just a home, but a status symbol. A place of pride that tells the world your story and your rise to the pinnacle of success.</p>
                        <div class="akshar-highlights">
                            <div class="akshar-hl-item"><i class="fa-solid fa-circle-check"></i><span>Premium 2, 3 &amp; 4 BHK Residences</span></div>
                            <div class="akshar-hl-item"><i class="fa-solid fa-circle-check"></i><span>RERA No. PRM/KA/RERA/1251/309/PR/051125/008225</span></div>
                            <div class="akshar-hl-item"><i class="fa-solid fa-circle-check"></i><span>Prime Location &mdash; Jayanagar, Bangalore</span></div>
                        </div>
                        <div class="akshar-btns">
                            <a href="akshar.html" class="btn-akshar-primary">Explore Project</a>
                            <a href="pdf/Opera-Akshar-broucher.pdf" class="btn-akshar-outline" target="_blank">Download Brochure</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- About Us Section End -->'''

new_content = pattern.sub(new_section, content)

if new_content != content:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Done! Section replaced.')
else:
    print('Pattern not found.')
