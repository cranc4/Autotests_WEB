import yaml
import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
# Данные для отправки письма
fromaddr = testdata.get("fromaddr")
toaddr = testdata.get("toaddr")
mypass = testdata.get("fromaddr_passwd")
reportname = "log.txt"

# Создание объекта MIMEMultipart
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Привет от питона (отчет по тестированию)"

# Добавляем файл во вложение
with open(reportname, "rb") as log:
    part = MIMEApplication(log.read(), Name=basename(reportname))
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(reportname)
    msg.attach(part)

letter = "Отчет о тестировании"

msg.attach(MIMEText(letter, "plain"))
server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()