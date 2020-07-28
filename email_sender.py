import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Hungtao Chou'
email['to'] = 'hungtao@gmail.com'
email['subject'] = 'you won one million dollars'

email.set_content(html.substitute({'name': 'HTC'}), 'html')
#email.set_content('I am just trying out python email function')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('htchou0808@gmail.com', 'beagle08')
	smtp.send_message(email)
	print('email sent!')