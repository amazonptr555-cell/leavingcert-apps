# Leaving Cert apps smart links

One share link per app: `https://amazonptr555-cell.github.io/leavingcert-apps/<app>/`.
iPhone/iPad go to the App Store, Android goes to Google Play (or a "coming soon" note), desktop sees both buttons.

- **Store links:** edit `apps.js`. When an Android app is released, paste its Play Store link into `android`.
- **New app:** `python3 make_page.py chemistry "Leaving Cert Chemistry Q&A" "One-line description"`, add `chemistry` to `apps.js`, put a 512x512 `icon.png` in the new folder.
- In each iOS app, set `PremiumConfig.shareLink` to that app's link.
