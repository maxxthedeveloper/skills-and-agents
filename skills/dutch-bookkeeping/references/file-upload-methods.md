# File Upload Methods (Bypassing Native File Picker)

Native file dialogs cannot be automated. Use these workarounds in order of preference.

## Method 1: JavaScript Base64 Injection (Preferred for Single Files)

Inject the PDF directly into the file input using DataTransfer API:

1. **Read the PDF as base64:**
   ```bash
   base64 -i "/Users/maxx/Documents/Finance/Receipts /2025/Q1-BTW-Bonnetjes/cursor_2025-01-08_110.42_INV-12345.pdf"
   ```

2. **Find the file input element** using `mcp__claude-in-chrome__read_page` or `find`

3. **Inject the file via JavaScript** using `mcp__claude-in-chrome__javascript_tool`:
   ```javascript
   // Replace BASE64_STRING with actual base64 data
   // Replace ref_X with the file input's ref ID
   const base64 = 'BASE64_STRING';
   const byteCharacters = atob(base64);
   const byteNumbers = new Array(byteCharacters.length);
   for (let i = 0; i < byteCharacters.length; i++) {
     byteNumbers[i] = byteCharacters.charCodeAt(i);
   }
   const byteArray = new Uint8Array(byteNumbers);
   const blob = new Blob([byteArray], { type: 'application/pdf' });
   const file = new File([blob], 'invoice.pdf', { type: 'application/pdf' });
   const dataTransfer = new DataTransfer();
   dataTransfer.items.add(file);
   const input = document.querySelector('[data-ref="ref_X"]') || document.querySelector('input[type="file"]');
   input.files = dataTransfer.files;
   input.dispatchEvent(new Event('change', { bubbles: true }));
   ```

4. **Verify upload succeeded** before proceeding

## Method 2: Slimme Inbox Bulk Email Upload (Preferred for Multiple Files)

Tellow's email-based upload bypasses file dialogs entirely. Send PDFs via command-line SMTP.

**Slimme Inbox email:** `maxpotze+6660264967c4b@inkomend.tellow.nl`

**Prerequisites (one-time setup):**
1. User needs a **Gmail App Password**: https://myaccount.google.com/apppasswords
2. Agent should ask user for password at runtime (don't store in code or config)

**Usage:**
```bash
# Ask user for their Gmail App Password, then run:
python3 ~/.claude/skills/dutch-bookkeeping/references/send_to_tellow.py "/Users/maxx/Documents/Finance/Receipts /2025/Q1-BTW-Bonnetjes/" "xxxx xxxx xxxx xxxx"
```

**Workflow:**
1. Download all invoices to the quarter folder (Phase 2)
2. Ask user for Gmail App Password (direct link: https://myaccount.google.com/apppasswords)
3. Run bulk send script with password as argument
4. Invoices appear in Tellow: **Inkoopfacturen** then **"Nog te verwerken"** tab
5. Process each invoice (see "Processing Invoices from Nog te verwerken" in SKILL.md)

## Method 3: User-Assisted Upload (Fallback)

If injection fails, guide the user:

1. Tell user exactly which file to upload with full path
2. Click the upload button to open native dialog
3. Wait for user to select file
4. Continue with categorization after upload completes
