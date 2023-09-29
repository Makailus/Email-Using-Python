#!/usr/bin/env python
# coding: utf-8

# In[13]:


pip install secure-smtplib


# In[17]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail SMTP server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'harshbro5080@gmail.com'
smtp_password = "qotl urth dpmv tifp"

# Email content
to_email = input("enter the receiver email")
subject = 'Test Email'
message = 'This is a test email sent from Python.'

# Create the email message
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Connect to Gmail's SMTP server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(smtp_username, to_email, msg.as_string())

    # Close the SMTP server connection
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print("An error occurred:", str(e))


# In[18]:


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail SMTP server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'harshbro5080@gmail.com'
smtp_password = 'qotl urth dpmv tifp'

# Email content
to_email = input("enter the recievers email address")
subject = 'Test Email'
message = 'This is a test email sent from Python.'

# Create the email message
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Connect to Gmail's SMTP server and send the email
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)
server.sendmail(smtp_username, to_email, msg.as_string())
server.quit()

print("Email sent successfully.")


# In[ ]:




