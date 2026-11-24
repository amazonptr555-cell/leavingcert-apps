"""Create the page for a new app:  python3 make_page.py <folder> "<App name>" "<one-line description>"
Then add the app to apps.js and drop a 512x512 icon.png into the folder."""
import html, os, sys

BASE = "https://leavingcertapps.ie"
TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name}</title>
<meta name="description" content="{desc}">
<!-- Link preview for WhatsApp, iMessage, Facebook (these don't run JavaScript, so they stay in the HTML) -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="{name}">
<meta property="og:title" content="{name}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{base}/{slug}/">
<meta property="og:image" content="{base}/{slug}/icon.png">
<meta property="og:image:width" content="512">
<meta property="og:image:height" content="512">
<meta name="twitter:card" content="summary">
<link rel="icon" href="icon.png">
<link rel="apple-touch-icon" href="icon.png">
<link rel="stylesheet" href="../style.css">
<script>window.LC_APP_ID = "{slug}";</script>
<script src="../apps.js"></script>
<script src="../smartlink.js"></script>
</head>
<body>
  <main class="card">
    <img class="icon" src="icon.png" alt="">
    <h1>{name}</h1>
    <p>{desc}</p>
    <a class="btn" id="ios" href="#">Download on the App Store</a>
    <a class="btn secondary" id="android" href="#">Get it on Google Play</a>
    <p class="note">The Android version is coming soon. It's available now on iPhone and iPad.</p>
  </main>
</body>
</html>
"""

slug, name, desc = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(slug, exist_ok=True)
with open(os.path.join(slug, "index.html"), "w") as f:
    f.write(TEMPLATE.format(base=BASE, slug=slug, name=html.escape(name), desc=html.escape(desc)))
print(f"Wrote {slug}/index.html -> {BASE}/{slug}/")
