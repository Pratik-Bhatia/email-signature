# Gmail Asset Hosting Instructions

To make your HTML email signature work flawlessly in Gmail, you **must host the signature images on your web server**. 

Gmail requires images to be publicly accessible over the internet via `https://`. Local files on your computer will break when sent in an email.

## 1. What You Need to Do

Upload the following **10 image files** (found in the `email-signature/assets/` folder) to your Officeneed website server so they sit exactly at:
`https://www.officeneed.in/email-signature/assets/[filename]`

### List of Assets to Upload:
1. `seamless-geometric-pattern.png`
2. `triangular-pattern-flipped.png`
3. `officeneed-logo.png`
4. `officeneed-wordmark.png`
5. `phone.png`
6. `email.png`
7. `website.png`
8. `linkedin.png`
9. `instagram.png`
10. `facebook.png`

## 2. Verify Your Upload
Once you have uploaded the files, open this link in your browser to test:
[https://www.officeneed.in/email-signature/assets/officeneed-logo.png](https://www.officeneed.in/email-signature/assets/officeneed-logo.png)

If the logo loads in your browser, your asset hosting is correctly configured!

---
**CRITICAL WARNING**: Do **NOT** attempt to copy the signature into Gmail before uploading these assets. If you do, the images will appear as broken icons to your recipients.
