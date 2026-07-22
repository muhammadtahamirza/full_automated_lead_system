import redis
from celery import Celery, shared_task
import smtplib
import time
from email.message import EmailMessage
from core.database import engine, Session
from features.mailboxes.models import MailAccount
from features.leads.models import Lead
from features.templates.models import Template


redis_client = redis.Redis(host='localhost', port=6379,db=0, decode_responses=True)

celery= Celery(
    name ="sendEmail",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)


@shared_task
def send_single_email( mailbox_id : int, lead_id : int, template_id : int ):
	"""
	This is the only part that actually waits and sends.
	It executes exactly when the 'countdown' timer hits zero.
	"""
	# fech from db
	with Session(engine) as db:
		mailbox = db.get(MailAccount, mailbox_id)
		lead = db.get(Lead, lead_id)
		template = db.get(Template, template_id)

	# setup sender email
	sender_email = mailbox.email
	smtp_server = mailbox.smtp_server
	port = mailbox.port
	password = mailbox.password


	lead_email = lead.email

	msg = EmailMessage()
	msg['Subject'] = template.subject
	msg['From'] = sender_email
	msg['To'] = lead_email
	msg.set_content(template.body)


	try:
		with smtplib.SMTP_SSL(smtp_server, port) as server:
			isLogin = server.login(sender_email, password)
			if not isLogin:
				return {
					"status" : f"not logined -  {sender_email}"
				}

			server.send_message(msg)
		print("Email sent successfully!")
		return {
			"status" : "Sent successfully"
		}
	except Exception as e:
		print(f"An error occurred: {e}")

		return {
			"status" : "Erorr server sidee"
		}



