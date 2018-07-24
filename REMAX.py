# Import smtplib for the actual sending function
import smtplib

# Import DateTime
import datetime

# Import the email modules we'll need
from email.message import EmailMessage
Body = '''Hello all,

The RE/MAX Defect List spreadsheet has been updated in it's entirety, but please feel free to inquire as to the status of individual tickets at your convenience as well. Please note, if we receive an update from a Dev team - then we sent a notification through the ticket as well.

RE/MAX Defect List
<HTTPS URL TO GOOGLE DOC>



Thank you,'''

msg = EmailMessage()
msg.set_content(Body)
# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = str(datetime.date.today()) + '- RE/MAX Defect List Updates'
msg['From'] = 'PRIVATE'
msg['To'] = 'PRIVATE'

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.starttls()
mail.login('USERNAME', 'PASS')
mail.send_message(msg)
mail.quit
