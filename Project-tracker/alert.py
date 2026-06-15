# alert.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

def send_alert(product_name, current_price, threshold, url):
    subject = f"🚨 Price Drop Alert: {product_name}"
    body = f"""
    Hi there!

    Great news! The price of "{product_name}" has dropped!

    ✅ Current Price : ₹{current_price}
    🎯 Your Threshold: ₹{threshold}
    🔗 Buy Now       : {url}

    Act fast before the price goes back up!

    — Price Tracker Bot 🤖
    """

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print(f"[EMAIL] Alert sent for {product_name}!")
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")