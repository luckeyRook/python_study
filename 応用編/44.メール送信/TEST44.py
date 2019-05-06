#44.メール送信
#smtplib
import smtplib

from email.mine.text import MIMEText
from email.header import Header
from email.utils import formatdate

from_address='from@xxx.xx.jp'
to_address='to@xxx.xx.jp'

charset='ISO-2202-JP'
subject='メールの件名です'
text='メールの本文です'

msg = MIMEText(text,'plain',charset)
msg['Subject'] =Header(subject,charset)
msg['From'] = from_address
msg['To'] =to_address
msg['Date'] =formatdate(localtime=True)

smtp=smtplib.SMTP('XX.XX.jp')
smtp.sendmail(from_address,to_address,msg.as_string())
smtp.close()
