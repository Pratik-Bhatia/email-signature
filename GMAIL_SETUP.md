# How to Install Your Signature in Gmail

Gmail does not offer an "HTML Source" editor for signatures. You cannot paste the raw HTML code. Instead, you must use the "Copy Rendered Output" method.

Follow these steps precisely:

## Prerequisite: Asset Hosting
Before beginning, you MUST complete the steps in `GMAIL_ASSET_HOSTING.md`. The images must be publicly hosted on your server first, otherwise they will be broken in Gmail.

## Step 1: Open the Copy-Ready File
Open **`gmail-copy-preview.html`** in your Chrome or Safari browser.
*Note: If your images are broken here, it means you haven't uploaded them to your server yet.*

## Step 2: Select and Copy
1. Click anywhere inside the browser window.
2. Press `Ctrl + A` (Windows) or `Cmd + A` (Mac) to select the entire signature.
3. Press `Ctrl + C` (Windows) or `Cmd + C` (Mac) to copy it to your clipboard.

## Step 3: Paste into Gmail
1. Open Gmail and go to **Settings** (the gear icon) > **See all settings**.
2. Scroll down to the **Signature** section.
3. Click **+ Create new** (or edit an existing one).
4. Click inside the empty signature text box.
5. Press `Ctrl + V` (Windows) or `Cmd + V` (Mac) to paste the signature.

## Step 4: Verify and Save
1. The signature should appear exactly as it did in the browser. 
2. Ensure you assign the signature to your email address under "Signature defaults".
3. Scroll to the very bottom of the Gmail settings page and click **Save Changes**.

## You're Done!
Compose a new email to verify the signature appears correctly at the bottom of the draft.
