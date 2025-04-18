import pandas as pd
import smtplib
import time
import random
from email.message import EmailMessage

# Load Excel data
df = pd.read_excel("tecmantras_scraped_data.xlsx")

# Email credentials
EMAIL_ACCOUNTS = [
    {"email": "mca.2023.b01@gmail.com", "123": "456"},
    {"email": "alex@gmail.com", "789": "123"}, 
]

# Email sending function
def send_email(to_email, name, company, sender_info):
    msg = EmailMessage()
    msg["Subject"] = f"Let's Collaborate, {name}"
    msg["From"] = sender_info["email"]
    msg["To"] = to_email

    # Plain text version
    text = f"""Hi {name},

I came across {company} while researching top companies in the software development space. Your work looks impressive!

I wanted to connect and see if there's any opportunity for collaboration where our team at Tecmantras
 could add value to your projects.

Let me know a good time for a quick chat. I’d love to hear about your current needs and explore how we can help.

Best regards,
Karishma
Tecmantras
"""

    msg.set_content(text)

    # Send using SMTP
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_info["alex@gmail.com"], sender_info["789"])
            smtp.send_message(msg)
            print(f"Sent to {to_email}")
    except Exception as e:
        print(f"Error sending to {to_email}: {e}")

# Start sending emails in batches
for i, row in df.iterrows():
    email = row.get("emails")
    if isinstance(email, list) and email:
        recipient = email[0]  # Pick the first email if multiple
        name = "there"  # If no name scraped
        company = row.get("email", "")
        sender = EMAIL_ACCOUNTS[i % len(EMAIL_ACCOUNTS)]
        send_email(recipient, name, company, sender)

        # Delay to avoid spam flags
        time.sleep(random.randint(10, 20))
