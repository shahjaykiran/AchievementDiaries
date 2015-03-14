from django.core.mail import EmailMessage
from datetime import datetime
import string
import random
from . import strings

def randomInviteId(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def sendActivationEmail(EMAIL,ACTIVATION_CODE):
	email = EmailMessage(strings.EMAIL_ACTIVATE_ACCOUNT_SUBJECT, strings.EMAIL_ACTIVATE_ACCOUNT_BODY%(EMAIL,ACTIVATION_CODE), to=[EMAIL])
	x=email.send()
	print "Respone :"+str(x)
	return 0

