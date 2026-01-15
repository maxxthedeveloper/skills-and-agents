---
name: dutch-bookkeeping
description: Dutch freelance (zzp) bookkeeping automation for Tellow. Use when the user asks to reconcile transactions, find missing invoices/receipts, download invoices from vendors, upload receipts to Tellow, handle BTW/VAT quarter administration, or manage their Dutch bookkeeping. Requires browser control to login to Tellow and vendor platforms via Google OAuth.
---

# Dutch Bookkeeping Skill

Automates quarterly BTW invoice reconciliation for Dutch freelancers using Tellow.

## User Configuration

- **Google account**: maxpotze2@gmail.com (for OAuth logins)
- **Receipts folder**: `/Users/maxx/Documents/Finance/Receipts /{year}/Q{quarter}-BTW-Bonnetjes/`
- **Bookkeeping software**: Tellow (tellow.nl)

## Core Workflow

### Phase 0: Pre-approve Browser Domains

**Before any browser actions, present a plan to pre-approve all domains for the session.**

Use `mcp__claude-in-chrome__update_plan` to request approval for all domains you'll visit:

```
domains: [
  // Core
  "tellow.nl",
  "app.tellow.nl",
  "accounts.google.com",
  "mail.google.com",  // For 2FA email verification

  // Stripe (many vendors use this)
  "billing.stripe.com",
  "invoice.stripe.com",

  // Known vendors from Q4 2025
  "cursor.com",
  "claude.ai",
  "console.anthropic.com",
  "anthropic.com",
  "openai.com",
  "platform.openai.com",
  "figma.com",
  "vercel.com",
  "convex.dev",
  "ngrok.com",
  "dashboard.ngrok.com",
  "supabase.com",
  "deel.com",
  "notion.so",
  "loom.com",
  "gumroad.com"
]
approach: [
  "Login to Tellow and collect all open transactions",
  "Download invoices from each vendor's billing portal",
  "Move invoices to Finance/Receipts folder",
  "Upload invoices to matching Tellow transactions"
]
```

**This grants permission for the entire session** — no more per-action prompts on approved domains.

### Phase 1: Collect & Plan (ALWAYS DO THIS FIRST)

**Before downloading anything, build a complete list of all missing transactions.**

1. Navigate to tellow.nl, login via Google OAuth (maxpotze2@gmail.com)
2. Go to: **Bankieren → Transacties**
3. Click filter icon (top right) → select "Open" status
4. Click calendar icon → select relevant quarter
5. Extract ALL transactions with "Open" status (red indicator = missing invoice)
6. **Create a todo list** with ALL transactions that need invoices:
   - Use the TodoWrite tool to create entries for each missing invoice
   - **IMPORTANT:** Capture the **EUR amount** from the bank transaction (this is the actual converted amount)
   - Format: `Download invoice: {vendor} - €{EUR_amount} ({date})`
   - Example: `Download invoice: Cursor - €92.50 (2025-12-29)`
   - This EUR amount will be needed later when processing invoices in "Nog te verwerken"
   - Group by vendor where possible (one login, multiple invoices)
7. Present the complete list to the user before proceeding
8. Ask user to confirm which invoices to collect (or all)

**Example todo list structure:**
```
- [ ] Download invoice: Cursor - €110.42 (2025-01-08)
- [ ] Download invoice: Cursor - €98.50 (2025-02-08)
- [ ] Download invoice: Vercel - €20.00 (2025-01-15)
- [ ] Download invoice: Figma - €15.00 (2025-02-01)
- [ ] Upload invoices to Tellow
```

### Phase 2: Download Invoices from Vendors

**Only proceed after Phase 1 is complete and user confirms.**

**CRITICAL: Always web search first to find invoice location.**

Vendor billing portals change constantly. Never assume paths. For each vendor:

1. Mark the todo item as in_progress
2. Web search: `"[vendor name]" download invoice billing portal`
3. Navigate to the billing/invoice section found in search results
4. Login via Google OAuth if available, otherwise platform-specific auth
5. Download ALL invoices for this vendor from the todo list
6. **⚠️ VERIFY DOWNLOAD BEFORE CONTINUING:**
   - Run: `ls -la ~/Downloads/*.pdf | head -20` to check for new PDF files
   - Confirm the invoice PDF actually exists in Downloads folder
   - **DO NOT rely on browser tabs as proof of download** (see Stripe warning below)
   - Only proceed once file is confirmed in Downloads
7. **Move verified file to the correct folder:**
   - Source: `/Users/maxx/Downloads/{downloaded_filename}.pdf`
   - Destination: `/Users/maxx/Documents/Finance/Receipts /{year}/Q{quarter}-BTW-Bonnetjes/`
   - Rename to: `{vendor}_{date}_{amount}_{invoice_number}.pdf` (e.g., `cursor_2025-01-08_110.42_INV-12345.pdf`)
   - Use Bash: `mv ~/Downloads/{file}.pdf ~/Documents/Finance/Receipts/{year}/Q{quarter}-BTW-Bonnetjes/{vendor}_{date}_{amount}_{invoice_number}.pdf`
8. **Verify file moved successfully:**
   - Run: `ls ~/Documents/Finance/Receipts/{year}/Q{quarter}-BTW-Bonnetjes/`
   - Confirm the renamed file exists before marking complete
9. Mark each downloaded invoice as completed in the todo list **ONLY after file verification**
10. **Close the vendor tab** once all invoices for that vendor are downloaded and verified

## ⚠️ CRITICAL: Stripe Invoice Download Warning

**Many vendors use Stripe for billing. Stripe invoice links are DECEPTIVE:**

- Clicking a Stripe invoice link **opens a PDF preview in a new browser tab**
- This is **NOT a download** — the file is NOT in your Downloads folder
- Opening 10 invoice tabs ≠ 10 downloaded files

**Correct Stripe download procedure:**
1. Click the invoice link → PDF opens in new tab
2. Look for a "Download" button on the Stripe invoice page, OR
3. Use browser's save function: `Cmd+S` or right-click → "Save As"
4. **ALWAYS verify** with `ls ~/Downloads/*.pdf` before proceeding
5. Close the preview tab only AFTER confirming the file exists in Downloads

**Never mark a Stripe invoice as downloaded based on:**
- ❌ A new tab opening
- ❌ Seeing the PDF in the browser
- ❌ The number of tabs open

**Only mark as downloaded when:**
- ✅ `ls ~/Downloads/` shows the actual PDF file
- ✅ File has been moved to the Receipts folder
- ✅ `ls` confirms file exists in destination

### Phase 3: Upload Invoices to Tellow

**Using the Search Bar:**
Tellow has a search bar at the top of the transactions list. Use it to quickly find transactions:
- Type the vendor name (e.g., "Cursor", "Vercel") to filter transactions
- This is faster than scrolling through all open transactions
- Search, upload invoice, clear search, repeat for next vendor

**Upload Process:**
1. Return to Tellow transaction list (filtered for "Open")
2. Use the search bar to find transactions by vendor name
3. For each transaction:
   - Click on the transaction to open details
   - Upload the matching invoice PDF (see File Upload Methods below)
   - **Categorization rules:**
     - **Transfers to "Max Potze"** → Mark as **"Kruispost"** (internal transaction between own accounts)
     - **All other expenses** → Select **"Zakelijk"** (business expense)
   - Verify the EUR amount on invoice matches transaction amount
   - For USD invoices: Tellow shows conversion (e.g., "128.02 USD, 1 USD = 0.86... EUR") — match the EUR result
4. Transaction status changes from "Open" to completed when invoice attached
5. Mark upload tasks as completed in the todo list

## ⚠️ File Upload Methods (Bypassing Native File Picker)

**Native file dialogs cannot be automated.** Use these workarounds:

### Method 1: JavaScript Base64 Injection (Preferred)

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

### Method 2: Slimme Inbox Bulk Email Upload (Preferred for Multiple Files)

Tellow's email-based upload bypasses file dialogs entirely. Send PDFs via command-line SMTP.

**Slimme Inbox email:** `maxpotze+6660264967c4b@inkomend.tellow.nl`

**Prerequisites (one-time setup):**
1. User needs a **Gmail App Password**: https://myaccount.google.com/apppasswords
2. Agent should ask user for password at runtime (don't store in code or config)

**Bulk send script** - sends each PDF in a folder as a separate email:

```python
import smtplib
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

GMAIL_USER = "maxpotze2@gmail.com"
GMAIL_APP_PASSWORD = "YOUR_APP_PASSWORD"  # Get from user
TELLOW_INBOX = "maxpotze+6660264967c4b@inkomend.tellow.nl"

def send_invoice(pdf_path):
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = TELLOW_INBOX
    msg['Subject'] = f"Invoice: {os.path.basename(pdf_path)}"
    msg.attach(MIMEText("Automated invoice upload", 'plain'))

    with open(pdf_path, 'rb') as f:
        part = MIMEBase('application', 'pdf')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(pdf_path)}"')
        msg.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.send_message(msg)
    print(f"✓ Sent: {os.path.basename(pdf_path)}")

def bulk_send(folder_path):
    pdfs = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    print(f"Found {len(pdfs)} PDFs to send")
    for pdf in pdfs:
        send_invoice(os.path.join(folder_path, pdf))
    print(f"Done! {len(pdfs)} invoices sent to Tellow Slimme Inbox")

if __name__ == "__main__":
    bulk_send(sys.argv[1])
```

**Usage:**
```bash
# Ask user for their Gmail App Password, then run:
python3 ~/.claude/skills/dutch-bookkeeping/references/send_to_tellow.py "/Users/maxx/Documents/Finance/Receipts /2025/Q1-BTW-Bonnetjes/" "xxxx xxxx xxxx xxxx"
```

**Workflow:**
1. Download all invoices to the quarter folder (Phase 2)
2. Ask user for Gmail App Password (direct link: https://myaccount.google.com/apppasswords)
3. Run bulk send script with password as argument
4. Invoices appear in Tellow → **Inkoopfacturen → "Nog te verwerken"** tab
5. Process each invoice (see "Processing Invoices from Nog te verwerken" below)

### Processing Invoices from "Nog te verwerken"

After bulk upload, invoices land in **Inkoopfacturen → "Nog te verwerken"** tab. Process each one:

1. Navigate to **Inkoopfacturen** page
2. Click **"Nog te verwerken"** tab (shows count of pending invoices)
3. For each invoice, click **"Verwerken"** button
4. Tellow auto-reads the invoice and pre-fills details
5. **⚠️ CRITICAL: Check for USD invoices and fix the amount:**
   - Look at the invoice PDF on the right side
   - If it shows **$ or USD** (e.g., "$100.00 USD"), Tellow may incorrectly auto-fill the same number as EUR
   - **This is WRONG** — $100 USD ≠ €100 EUR
   - **Fix:** Look up the correct EUR amount from your todo list (captured in Phase 1 from bank transactions)
   - Example: Todo says `Cursor - €92.50 (2025-12-29)` → enter **€92.50** as the amount
   - Update the "Bedrag" (amount) field to match the EUR amount from your todo list
   - **BTW-tarief:** Select **"Buiten EU"** for non-EU vendors (US companies like Cursor, Vercel, OpenAI, etc.) — this applies 21% BTW
6. Verify/adjust other fields:
   - **Leverancier** (vendor): confirm or select correct one
   - **Datum** (date): invoice date
   - **Type kosten**: select appropriate category (usually "Algemene kosten")
   - **Categorie**: select **"Zakelijk"** (business expense)
7. **Match to transaction**: Scroll down to link to bank transaction
   - Select the correct transaction (amount should now match!)
   - If no match suggested, search by date or vendor name
8. Click **"Boeken"** (book) to complete
   - **Note:** After booking, Tellow automatically loads the next invoice in "Nog te verwerken" — no need to navigate back to the list
9. Continue processing each invoice as it loads automatically

**USD Conversion Summary:**
- Invoice shows: $100.00 USD
- Tellow auto-fills: €100,00 ❌ WRONG
- Bank transaction shows: €92,50 (actual conversion)
- Correct entry: €92,50 ✅

### Recovery: Finding EUR Amounts (if not captured in Phase 1)

If you forgot to capture EUR amounts in the todo list during Phase 1, recover them as follows:

1. **Open a second tab** with Tellow → **Bankieren → Transacties**
2. Filter for "Open" status to see unprocessed transactions
3. For each invoice you're processing in "Nog te verwerken":
   - Note the **vendor name** and **date** from the invoice PDF
   - Switch to the Transacties tab
   - **Use the search bar** to find the transaction by vendor name
   - The transaction shows the **actual EUR amount** (bank's conversion rate)
   - Switch back to "Nog te verwerken" and enter the correct EUR amount
4. **Pro tip:** Before processing, screenshot or list all open transactions with their EUR amounts to avoid switching back and forth repeatedly

### Fallback: ECB Rate Lookup (when bank EUR amount unavailable)

**Use this when the EUR amount cannot be found in bank transactions** (e.g., unpaid invoice, credit card not yet synced, or manual entry needed).

Per Dutch tax law ([Belastingdienst](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/bereken_het_bedrag/hoe_berekent_u_het_btw_bedrag/)), you must use the official ECB rate from the **invoice date**.

**Step 1: Get the ECB rate for the invoice date**

Use the ECB Statistical Data Warehouse API:

```bash
# Replace YYYY-MM-DD with invoice date
curl -s "https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=YYYY-MM-DD&endPeriod=YYYY-MM-DD&format=csvdata" | tail -1 | cut -d',' -f8
```

Example for January 10, 2025:
```bash
curl -s "https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2025-01-10&endPeriod=2025-01-10&format=csvdata" | tail -1 | cut -d',' -f8
# Returns: 1.0304 (meaning 1 EUR = 1.0304 USD)
```

**Step 2: Calculate EUR amount**

The ECB rate shows EUR→USD. To convert USD to EUR:

```
EUR_amount = USD_amount / ECB_rate
```

Example: $100 USD on a day when ECB rate is 1.0850
```
EUR_amount = 100 / 1.0850 = €92.17
```

**Step 3: Document the conversion**

When using ECB rate (not bank rate), add a note in Tellow's description field:
```
Converted from $XXX USD using ECB rate X.XXXX on YYYY-MM-DD
```

**Quick conversion script:**

```bash
# Usage: convert_usd_to_eur.sh <USD_amount> <invoice_date>
# Example: ./convert_usd_to_eur.sh 100.00 2025-01-15

USD_AMOUNT=$1
INVOICE_DATE=$2

ECB_RATE=$(curl -s "https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=${INVOICE_DATE}&endPeriod=${INVOICE_DATE}&format=csvdata" | tail -1 | cut -d',' -f8)

if [ -z "$ECB_RATE" ]; then
  echo "No rate found for $INVOICE_DATE (weekend/holiday?). Try adjacent business day."
  exit 1
fi

EUR_AMOUNT=$(echo "scale=2; $USD_AMOUNT / $ECB_RATE" | bc)
echo "USD $USD_AMOUNT → EUR $EUR_AMOUNT (ECB rate: $ECB_RATE on $INVOICE_DATE)"
```

**Note:** ECB doesn't publish rates on weekends/holidays. If invoice date has no rate, use the **previous business day's rate** (this is the legally accepted method).

### Method 3: User-Assisted Upload (Fallback)

If injection fails, guide the user:

1. Tell user exactly which file to upload: "Please select: `/Users/maxx/Documents/Finance/Receipts /2025/Q1-BTW-Bonnetjes/cursor_2025-01-08_110.42_INV-12345.pdf`"
2. Click the upload button to open native dialog
3. Wait for user to select file
4. Continue with categorization after upload completes

### Handling Deel Invoices (Sales/Income)

**Deel invoices are NOT purchases — they are income/sales from client payments.**

1. Download all Deel invoice PDFs during Phase 2
2. Save them in a special subfolder: `/Users/maxx/Documents/Finance/Receipts /{year}/Q{quarter}-BTW-Bonnetjes/sales ultrathink/`
   - Create the folder if it doesn't exist: `mkdir -p "~/Documents/Finance/Receipts /{year}/Q{quarter}-BTW-Bonnetjes/sales ultrathink/"`
3. **Research how to create "facturen" (invoices) in Tellow:**
   - Web search: `tellow factuur maken aanmaken`
   - Navigate to the invoicing/facturen section in Tellow
   - Understand the process for registering sales/income
4. **Ask user for approval before submitting any sales invoices to Tellow**
5. Present findings to user: "I've downloaded {n} Deel invoices to the sales folder. Here's how to register them as facturen in Tellow: [explain process]. Should I proceed?"

### Handling 2FA Email Verification

**When a vendor login requires email-based 2FA:**

1. When you see a "Check your email" or "Verify via email" prompt, pause the vendor login
2. Open a new tab and navigate to `mail.google.com`
3. The verification email should be the most recent email in the inbox
4. Click the login/verification link in the email
5. Return to the vendor tab — you should now be authenticated
6. Continue with the invoice download process

## EUR/USD Handling

Tellow automatically converts USD transactions to EUR using bank exchange rate. The transaction displays both the original USD amount and the final EUR amount. When uploading: match the **EUR amount shown in Tellow**, not the USD amount on the invoice.

## Common Vendors Reference

See `references/vendors.md` for known vendor billing portal patterns. **Always verify with web search first** — this list is a fallback reference only.

## Skip List (Inaccessible Invoices)

Some vendors don't have web-accessible invoice portals. Skip these and let the user handle manually:

- **Bunq** — invoices only available in mobile app
- Add others as discovered

When encountering a vendor with no accessible billing portal, note it in the final summary and move on.

## Error Handling

- **Can't find invoice portal**: Try searching `"[vendor]" billing history download PDF`
- **Invoice amount doesn't match**: Check for partial refunds, currency conversion, or split transactions
- **Platform requires non-Google auth**: Ask user to complete login manually
- **Invoice not available yet**: Some platforms delay invoice generation; note and retry later
