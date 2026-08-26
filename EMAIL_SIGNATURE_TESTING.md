# Email Signature Testing Checklist

Before deploying the signature to the entire team, please use this checklist to ensure everything works perfectly across different email clients and devices.

## 🔗 Link Validation
- [ ] **Logo Click:** Does clicking the Officeneed logo open `https://www.officeneed.in/`?
- [ ] **Website Click:** Does clicking the website link open `https://www.officeneed.in/`?
- [ ] **Phone Click:** Does clicking the phone number prompt a call to `+91 797279 7965` (especially on mobile)?
- [ ] **Email Click:** Does clicking the email address open a new draft to `contact@officeneed.in`?
- [ ] **LinkedIn Click:** Does clicking the LinkedIn icon open `https://www.linkedin.com/company/officeneed-in/`?
- [ ] **Instagram Click:** Does clicking the Instagram icon open the correct profile?
- [ ] **Facebook Click:** Does clicking the Facebook icon open the correct profile?
- [ ] **YouTube Click:** Does clicking the YouTube icon open the correct channel?

## 🖼️ Image Assets
- [ ] **Images Loading:** Do all images load correctly from the remote server?
- [ ] **Image Alt Text:** Hover over the images to verify alt text (e.g., "Officeneed", "LinkedIn").
- [ ] **Broken Image Fallback:** If images are blocked by the email client, is the layout still readable and do the alt texts appear?

## 📱 Client Compatibility
Send a test email containing the signature to the following clients:
- [ ] **Gmail (Desktop Web):** Renders correctly with proper alignment and spacing.
- [ ] **Gmail (Mobile App):** Scales appropriately without horizontal scrolling.
- [ ] **Outlook (Desktop App):** Renders correctly without breaking table structure.
- [ ] **Outlook (Web):** Displays correctly.
- [ ] **Apple Mail (Desktop):** Displays correctly.
- [ ] **Apple Mail (iOS):** Scales properly on iPhone.

## 🎨 Visual Quality Assurance
- [ ] **Signature Alignment:** Are all elements vertically and horizontally aligned as expected?
- [ ] **Font Rendering:** Does the text appear in Arial/Helvetica/sans-serif?
- [ ] **Mobile Scaling:** Does the signature narrow gracefully on small screens without breaking content?
- [ ] **No Unexpected Styling:** Are links their proper color (no unexpected blue underlines from default browser styles)?
- [ ] **Dark Mode Support:** Test in a dark mode email client to ensure the signature remains readable (images may need a subtle white glow if they disappear in dark mode, though the design uses a light background table).
