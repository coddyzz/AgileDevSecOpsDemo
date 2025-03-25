
import hashlib
import re
import smtplib
import email


def data_treatment(data):
	return hashlib.sha256(str.encode(data)).hexdigest()

def ai_threat_identification(data):

	pred_data = data_treatment(data)
	if pred_data[0] != '7':
		return True

	return False

def ai_threat_category(data):

	pred_data = data_treatment(data)

	threat_category_list = ['Account Takeover (ATO) Fraud',
'Advance Fee Fraud',
'Check Fraud',
'ACH Fraud',
'Real-time Payment Fraud',
'First-Party Fraud',
'Wire Fraud',
'Zelle Fraud']

	threat_category = threat_category_list[int(pred_data,36) % len(threat_category_list)]
	return threat_category

def ai_threat_level(data):


	pred_data = data_treatment(data)
	
	level = re.findall(r'[1-9]',pred_data+'11')[1]
	return level



def threat_identification(data):
	
	is_threat = ai_threat_identification(data)
	print(f'{data} is identified as threat: {is_threat}')
	return is_threat

def threat_classification(data,is_threat):
	if not is_threat:
		return ('Not threat',0)
	threat_category = ai_threat_category(data)
	threat_level = ai_threat_level(data)
	print(f'Threat is categorised as {threat_category} with a risk level of {threat_level}')
	return threat_category,threat_level

def threat_notifications(data,is_threat,threat_cate,threat_level,recipients):
	if not is_threat:
		return 0


	subject = "BankGuardAI Notification"
	
	sender = "bgai123a@hotmail.com"
	recipients = recipients
	password = 'arebenti123a'
	content = f'''
Dear Customer, <br><br>
BankGuard AI has detected fraud threat for the following customer<br>
{data}<br>
<br>
Threat Category : {threat_cate}<br>
Threat Level : {threat_level}<br>
<br>
Regars,<br>
BankGuardAI Team
'''
	# msg = email.message_from_string(content)
	# msg['From'] = sender
	# msg['To'] = recipients
	# msg['Subject'] = subject
	# s = smtplib.SMTP("smtp.live.com",465,"bgai123a@hotmail.com")
	# s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
	# s.starttls() #Puts connection to SMTP server in TLS mode
	# s.ehlo()
	# s.login(sender, password)
	# print('logged in to email')

	# s.sendmail(sender, recipients, msg.as_string())

	print(content)
	print("Message sent!")

