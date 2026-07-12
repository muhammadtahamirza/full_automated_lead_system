import smtplib

from email.message import EmailMessage
# 1. Email configuration
smtp_server = 'mail.spacemail.com'
port = 465
sender_email = 'taha@leadhoppers.dev'
password = 'tahamir4846G@'


msg = EmailMessage()
msg['Subject'] = 'Hello from Python'
msg['From'] = sender_email
msg['To'] = 'tahaseopro@gmail.com'
msg.set_content('This is an automated email sent using Spacemail and Python.')


# 3. Connect and send using SSL
try:
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        isLogin = server.login(sender_email, password)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
