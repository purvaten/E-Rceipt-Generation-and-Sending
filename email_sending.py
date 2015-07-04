def send_email(sender_email="",sender_pass="",receiver_email="",subject="",text_msg="",pdf_file=""):
	# Import smtplib for the actual sending function
	import smtplib

	# For guessing MIME type
	import mimetypes

	# Import the email modules we'll need
	import email
	import email.mime.application
	print "Sending email..."+sender_email
	# Create a text/plain message
	msg = email.mime.Multipart.MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = sender_email
	msg['To'] = receiver_email

	# The main body is just another attachment
	body = email.mime.Text.MIMEText(text_msg)
	msg.attach(body)

	# PDF attachment
	filename=pdf_file+".pdf"
	fp=open(filename,'rb')
	att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
	fp.close()
	att.add_header('Content-Disposition','attachment',filename=filename)
	msg.attach(att)

	# send via Gmail server
	# NOTE: my ISP, Centurylink, seems to be automatically rewriting
	# port 25 packets to be port 587 and it is trashing port 587 packets.
	# So, I use the default port 25, but I authenticate. 
	s = smtplib.SMTP('smtp.gmail.com')
	s.ehlo()
	s.starttls()
	s.login(sender_email,sender_pass)
	s.sendmail(receiver_email,[receiver_email], msg.as_string())
	s.quit()