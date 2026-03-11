# Sales Invoices (Facturen / Income)

Sales invoices (verkoopfacturen) are invoices YOU send to clients for work performed -- the opposite of purchase invoices (inkoopfacturen).

Common sources of sales invoices:
- **Deel** -- client payments processed through Deel platform
- **Direct clients** -- invoices you create and send yourself
- **Other freelance platforms** -- any platform that pays you for work

## Step 1: Download Existing Sales Invoices (e.g., Deel)

1. During Phase 2, also download sales invoices from platforms like Deel
2. Save them in a special subfolder: `/Users/maxx/Documents/Finance/Receipts /{year}/Q{quarter}-BTW-Bonnetjes/sales/`
   - Create the folder if it doesn't exist: `mkdir -p "~/Documents/Finance/Receipts /{year}/Q{quarter}-BTW-Bonnetjes/sales/"`
3. Name format: `{client}_{date}_{amount}_{invoice_number}.pdf`

## Step 2: Upload Sales Invoices to Tellow

### Option A: Upload existing external invoices (e.g., Deel invoices)

1. Navigate to **Verkoop** then **Facturen**
2. Click the **three-dot menu** and select **"Upload verkoopfactuur"**
3. Select the client/contact from your address book (or add new contact)
4. Enter the invoice details from the PDF:
   - Invoice number
   - Invoice date
   - Amount (EUR)
   - Description of services
5. Click **"Upload factuur"** at the bottom to attach the PDF
6. Click **"Definitief maken"** to finalize

### Option B: Create new sales invoices directly in Tellow

Use this when you need to bill a client and don't have an external invoice yet:

1. Navigate to **Verkoop** then **Facturen**
2. Click **"Factuur opmaken"** (Create Invoice)
3. The invoice creation screen has these sections:

**Header options:**
- Toggle **"Verstuur als Engelse factuur"** (Send as English invoice) -- enable for non-Dutch clients
- **"Kies factuursjabloon"** dropdown -- select template (default: "Standaardsjabloon")
- **"Bekijk factuur"** button -- preview the invoice

**Invoice details row:**
- **Klant** (Client): Click "Kies klant" to select existing client (e.g., "Solana") or add new
- **Factuurdatum** (Invoice date): Auto-filled with today's date
- **Geldigheidsduur in dagen** (Payment terms): Default 30 days
- **Factuurtype**: Usually "Normaal"
- **"Toon optionele velden"** -- expand for additional fields

**Line items section:**
- **Aantal** (Quantity): Number of units/hours
- **Omschrijving** (Description): What you're billing for (e.g., "Product Design Services - December 2025")
- **Bedrag** (Amount): Price per unit, excl. BTW
- **Korting** (Discount): Optional percentage discount
- **Btw** (VAT): Select rate (21%, 9%, 0%, or "Vrijgesteld")
- **Totaal**: Auto-calculated
- Click **"+ Regel toevoegen"** to add more line items

**Footer section:**
- **Aanvullend bericht (optioneel)**: Pre-filled payment instructions
- **Subtotaal** and **Totaal incl. btw**: Auto-calculated
- **"Voeg bijlage toe"** or drag files to attach documents

**Action buttons:**
- **"Annuleer"** (Cancel) -- discard without saving
- **"Opslaan"** (Save) -- save as draft, can edit later
- **"Definitief maken"** (Finalize) -- lock invoice with auto-numbering, ready to send

**Known clients:** Solana (product design work)

**First-time setup tip:** Configure your invoice template first via **Instellingen** then **Factuurinstellingen**:
- Upload your company logo
- Set default payment terms (e.g., 30 dagen)
- Add standard footer text (bank details, KvK number, BTW number)

## Step 3: Link Sales Invoices to Incoming Bank Transactions

After uploading/creating sales invoices, link them to the corresponding incoming payments:

### Method A: From Bank Transactions (recommended)

1. Go to **Bankieren** then **Transacties**
2. Filter for **incoming (positive)** transactions that are "Open"
3. Click the relevant incoming payment
4. Select **"Zakelijk"** (Business)
5. Click the matching sales invoice from the list
   - If not listed, click **"Upload een factuur"** to add it
6. Click **"Klaar"** (Done)

### Method B: From the Invoice

1. Go to **Verkoop** then **Facturen**
2. Click the relevant sales invoice
3. Under **"Nog te ontvangen"** (Still to receive), click **"Voeg een betaalwijze of transactie toe"**
4. Select **"Zakelijke rekening"** (Business account)
5. Choose the correct incoming transaction
6. Click **"Klaar"** (Done)

**For partial payments:** Repeat the linking process for each partial payment until the full invoice amount is accounted for.

## Deel-Specific Workflow

Deel invoices are pre-generated PDFs from client payments:

1. Download Deel invoice PDFs during Phase 2
2. Save to `/Users/maxx/Documents/Finance/Receipts /{year}/Q{quarter}-BTW-Bonnetjes/sales/`
3. In Tellow: **Verkoop** then **Facturen** then three-dot menu then **Upload verkoopfactuur**
4. Add "Deel" or the end-client as the contact
5. Enter details from the Deel invoice PDF
6. Upload the PDF and finalize
7. Link to the corresponding incoming Deel bank transaction

**Ask user for approval before uploading sales invoices to Tellow** -- sales affect revenue reporting and BTW calculations.
