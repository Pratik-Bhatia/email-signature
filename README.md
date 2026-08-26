# Officeneed HTML Email Signature

This directory contains the production-ready HTML email signature for **Officeneed**.

## What Was Created
We have transformed the original single-image visual design into a robust, table-based HTML email signature. Every text piece is selectable, and every contact detail and social icon is an independent, clickable link.

### Files Included
- **`signature.html`**: The main HTML source for the email signature. This contains the production version with absolute `https://` URLs pointing to the intended asset host.
- **`preview.html`**: A localized preview file that uses relative paths (`./assets/`) so you can visually verify the signature right now on your computer.
- **`preview.png`**: An image snapshot of the signature as rendered by a browser.
- **`assets/`**: Contains all required individual icon and logo files (`officeneed-logo.png`, `officeneed-wordmark.png`, `linkedin.png`, etc.).
- **`GMAIL_SETUP.md`**: Step-by-step instructions for installing this signature in Gmail.
- **`EMAIL_SIGNATURE_TESTING.md`**: A comprehensive checklist to ensure your signature works properly across all platforms.

## URLs Configured
The following links are fully configured in the `signature.html`:
- **Website:** `https://www.officeneed.in/` (Clickable URL and Logo)
- **Email:** `mailto:contact@officeneed.in`
- **Phone:** `tel:+917972797965`
- **LinkedIn:** `https://www.linkedin.com/company/officeneed-in/`

## URLs Requiring Updates
The following URLs were not provided and contain placeholders in the `signature.html` code. Please open `signature.html` in a code editor and search for these exact strings to replace them with your actual profiles:
- `[INSERT EXACT OFFICENEED INSTAGRAM URL HERE]`
- `[INSERT EXACT OFFICENEED FACEBOOK URL HERE]`
- `[INSERT EXACT OFFICENEED YOUTUBE URL HERE]`

If you do not have profiles for these platforms, you should safely delete the corresponding `<td>...</td>` blocks that wrap each icon in the HTML.

## Hosting Assets
Email signatures cannot embed local images directly. The assets in the `assets/` folder MUST be uploaded to a public web server. By default, the HTML code expects them to be located at:
`https://pratik-bhatia.github.io/email-signature/assets/`

If you host them elsewhere, perform a find-and-replace in `signature.html` for `https://pratik-bhatia.github.io/email-signature/assets/` and replace it with your actual path.

## How to Update the Signature Later
If you need to change an employee's name or contact details:
1. Open `signature.html` in any code or text editor.
2. Locate the text you want to change (e.g., "Team Officeneed" or "Operations").
3. Carefully replace the text without altering any surrounding HTML tags (`<td>`, `<tr>`, `<font>`, etc.).
4. Save the file and follow the `GMAIL_SETUP.md` instructions to load the updated version into your email client.
