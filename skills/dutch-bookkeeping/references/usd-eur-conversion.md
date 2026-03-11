# USD/EUR Conversion Handling

## Priority: Use Bank Transaction EUR Amount

Always prefer the EUR amount from the bank transaction (captured in Phase 1 todo list). This is the actual amount debited and is the most accurate.

## Processing USD Invoices in "Nog te verwerken"

After bulk upload, invoices land in **Inkoopfacturen** then **"Nog te verwerken"** tab. For USD invoices:

1. Look at the invoice PDF on the right side
2. If it shows $ or USD (e.g., "$100.00 USD"), Tellow may incorrectly auto-fill the same number as EUR
3. **This is WRONG** -- $100 USD is not the same as 100 EUR
4. **Fix:** Look up the correct EUR amount from your todo list (captured in Phase 1 from bank transactions)
5. Example: Todo says `Cursor - 92.50 EUR (2025-12-29)` then enter 92.50 as the amount
6. Update the "Bedrag" (amount) field to match the EUR amount from your todo list
7. **BTW-tarief:** Select **"Buiten EU"** for non-EU vendors (US companies like Cursor, Vercel, OpenAI, etc.) -- this applies 21% BTW

**USD Conversion Summary:**
- Invoice shows: $100.00 USD
- Tellow auto-fills: 100,00 EUR (WRONG)
- Bank transaction shows: 92,50 EUR (actual conversion)
- Correct entry: 92,50 EUR

## Recovery: Finding EUR Amounts (If Not Captured in Phase 1)

If you forgot to capture EUR amounts in the todo list during Phase 1:

1. **Open a second tab** with Tellow: **Bankieren** then **Transacties**
2. Filter for "Open" status to see unprocessed transactions
3. For each invoice you're processing in "Nog te verwerken":
   - Note the vendor name and date from the invoice PDF
   - Switch to the Transacties tab
   - Use the search bar to find the transaction by vendor name
   - The transaction shows the actual EUR amount (bank's conversion rate)
   - Switch back to "Nog te verwerken" and enter the correct EUR amount
4. **Pro tip:** Before processing, list all open transactions with their EUR amounts to avoid switching back and forth

## Fallback: ECB Rate Lookup

**Use this when the EUR amount cannot be found in bank transactions** (e.g., unpaid invoice, credit card not yet synced, or manual entry needed).

Per Dutch tax law (Belastingdienst), you must use the official ECB rate from the invoice date.

**Step 1: Get the ECB rate for the invoice date**

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

The ECB rate shows EUR to USD. To convert USD to EUR:
```
EUR_amount = USD_amount / ECB_rate
```

Example: $100 USD on a day when ECB rate is 1.0850:
```
EUR_amount = 100 / 1.0850 = 92.17 EUR
```

**Step 3: Document the conversion**

When using ECB rate (not bank rate), add a note in Tellow's description field:
```
Converted from $XXX USD using ECB rate X.XXXX on YYYY-MM-DD
```

**Note:** ECB does not publish rates on weekends/holidays. If invoice date has no rate, use the previous business day's rate (this is the legally accepted method).
