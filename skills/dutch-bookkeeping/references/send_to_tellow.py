#!/usr/bin/env python3
"""
Bulk send invoices to Tellow Slimme Inbox via Gmail SMTP.
Each PDF is sent as a separate email with delays to avoid spam filters.

Usage:
    python3 send_to_tellow.py <folder_path> <gmail_app_password> [delay_seconds]

Example:
    python3 send_to_tellow.py "/path/to/invoices/" "xxxx xxxx xxxx xxxx" 5

Rate Limiting:
- Gmail SMTP allows ~100 emails/day for free accounts
- Default 5-second delay between emails to avoid spam filters
- For 28 invoices: ~2.5 minutes total

App Password:
- Get from: https://myaccount.google.com/apppasswords
- If auth fails, generate a NEW app password (old ones can become invalid)
"""

import smtplib
import os
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

GMAIL_USER = "maxpotze2@gmail.com"
TELLOW_INBOX = "maxpotze+6660264967c4b@inkomend.tellow.nl"
DEFAULT_DELAY = 5  # seconds between emails


def send_invoice(pdf_path: str, app_password: str) -> bool:
    """Send a single PDF invoice to Tellow Slimme Inbox."""
    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = TELLOW_INBOX
        msg['Subject'] = f"Invoice: {os.path.basename(pdf_path)}"
        msg.attach(MIMEText("Automated invoice upload via bookkeeping skill", 'plain'))

        with open(pdf_path, 'rb') as f:
            part = MIMEBase('application', 'pdf')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename="{os.path.basename(pdf_path)}"'
            )
            msg.attach(part)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_USER, app_password)
            server.send_message(msg)

        return True

    except smtplib.SMTPAuthenticationError as e:
        print(f"\n❌ Authentication failed!")
        print(f"   Error: {e}")
        print(f"\n   Fix: Generate a NEW app password at:")
        print(f"   https://myaccount.google.com/apppasswords")
        print(f"\n   Then re-run this script with the new password.")
        return False

    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def bulk_send(folder_path: str, app_password: str, delay: int = DEFAULT_DELAY) -> tuple:
    """Send all PDFs in a folder to Tellow Slimme Inbox with rate limiting."""
    if not os.path.isdir(folder_path):
        print(f"Error: Folder not found: {folder_path}")
        sys.exit(1)

    pdfs = sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')])

    if not pdfs:
        print(f"No PDF files found in: {folder_path}")
        return 0, 0

    total = len(pdfs)
    estimated_time = total * delay

    print(f"╔══════════════════════════════════════════════════════════════╗")
    print(f"║  Tellow Slimme Inbox Bulk Upload                             ║")
    print(f"╠══════════════════════════════════════════════════════════════╣")
    print(f"║  PDFs to send: {total:<46} ║")
    print(f"║  Delay between emails: {delay} seconds{' ':<28} ║")
    print(f"║  Estimated time: ~{estimated_time // 60}m {estimated_time % 60}s{' ':<36} ║")
    print(f"║  Target: {TELLOW_INBOX:<43} ║")
    print(f"╚══════════════════════════════════════════════════════════════╝")
    print()

    success = 0
    failed = 0
    auth_failed = False

    for i, pdf in enumerate(pdfs, 1):
        pdf_path = os.path.join(folder_path, pdf)

        # Progress indicator
        progress = f"[{i}/{total}]"
        print(f"{progress} Sending: {pdf[:50]}...", end=" ", flush=True)

        if send_invoice(pdf_path, app_password):
            print("✓")
            success += 1
        else:
            if "Authentication" in str(sys.exc_info()[1]):
                auth_failed = True
                break
            print("✗")
            failed += 1

        # Rate limiting: wait between emails (except after last one)
        if i < total and not auth_failed:
            print(f"      ⏳ Waiting {delay}s to avoid spam filters...", end="\r")
            time.sleep(delay)
            print(" " * 50, end="\r")  # Clear the waiting message

    print()
    print(f"{'═' * 50}")
    print(f"  Results: ✓ Sent: {success}  ✗ Failed: {failed}")
    if success > 0:
        print(f"  Invoices will appear in Tellow 'Uitgaven' shortly")
    print(f"{'═' * 50}")

    return success, failed


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    folder = sys.argv[1]
    password = sys.argv[2]
    delay = int(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_DELAY

    bulk_send(folder, password, delay)
