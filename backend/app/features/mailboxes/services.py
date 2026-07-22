from .models import MailAccount
import smtplib


def loginMailbox(mailbox : MailAccount):
	try:
		with smtplib.SMTP_SSL(mailbox.smtp_server, mailbox.port) as server:
			server.login(mailbox.email, mailbox.password)
		return True

	except smtplib.SMTPAuthenticationError as e:
		raise ValueError("authentication failed, pass/username incorrect")
	except Exception as e:
		raise ValueError(f"An error occurred: {e}")

