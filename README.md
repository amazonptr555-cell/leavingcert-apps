# Leaving Cert apps smart links

One share link per app: `https://leavingcertapps.ie/<app>/`.
iPhone/iPad go to the App Store, Android goes to Google Play (or a "coming soon" note), desktop sees both buttons.

- **Store links:** edit `apps.js`. When an Android app is released, paste its Play Store link into `android`.
- **New app:** `python3 make_page.py chemistry "Leaving Cert Chemistry Q&A" "One-line description"`, add `chemistry` to `apps.js`, put a 512x512 `icon.png` in the new folder.
- In each iOS app, set `PremiumConfig.shareLink` to that app's link.

## Referral discount (WhatsApp share)

Each iOS app's paywall has a "Get X% off" button that opens WhatsApp with that app's link from this site.
Once WhatsApp opens, the paywall sells `<productID>.referral` (a cheaper non-consumable that unlocks the same course) instead of the standard product.

| App | Link | Standard product | Referral product |
|---|---|---|---|
| Biology | `/biology/` | `com.FinalLeavingBio.fullcourse` | `com.FinalLeavingBio.fullcourse.referral` |
| Business | `/business/` | `LCBusiness.fullcourse` | `LCBusiness.fullcourse.referral` |
| Chemistry | `/chemistry/` | `LeavingCertChemistry.fullcourse` | `LeavingCertChemistry.fullcourse.referral` |
| Economics | `/economics/` | `com.FinalLeavingEcon.fullcourse` | `com.FinalLeavingEcon.fullcourse.referral` |
| French | `/french/` | `com.FinalLeavingFrench.fullcourse` | `com.FinalLeavingFrench.fullcourse.referral` |
| Geography | `/geography/` | `com.FinalLeavingGeo.fullcourse` | `com.FinalLeavingGeo.fullcourse.referral` |
| German | `/german/` | `com.FinalLeavingGerman.fullcourse` | `com.FinalLeavingGerman.fullcourse.referral` |
| History | `/history/` | `com.FinalLeavingHist.fullcourse` | `com.FinalLeavingHist.fullcourse.referral` |
| Home Economics | `/home-economics/` | `com.FinalLeavingHomeEc.fullcourse` | `com.FinalLeavingHomeEc.fullcourse.referral` |
| Spanish | `/spanish/` | `com.FinalLeavingSpanish.fullcourse` | `com.FinalLeavingSpanish.fullcourse.referral` |

The share button only appears when the App Store returns both products, so an app is safe to ship before its referral product is approved.
