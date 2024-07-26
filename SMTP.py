import smtplib
from email.mime.text import MIMEText

mail_username = 'email que enviara'
mail_password = 'senha do email que enviara'
from_addr = 'email que enviara'
to_addrs = ['email que recebera']

HOST = 'smtp-mail.outlook.com'
PORTA = 587

smtp = smtplib.SMTP(HOST, PORTA)
smtp.ehlo()
print('Conectando...')

# conexão TLS
smtp.starttls()

try:
    print('Login...')
    smtp.login(mail_username, mail_password)
except smtplib.SMTPAuthenticationError as e:
    print(f'ERRO DE LOGIN ****: {e}')

msg = MIMEText('A conexão SMTP foi executada com sucesso o firewall não impediu a execuçao.')
msg['From'] = from_addr
msg['To'] = ', '.join(to_addrs)
msg['Subject'] = 'Teste SMTP'

print(msg.as_string())

try:
    smtp.sendmail(from_addr, to_addrs, msg.as_string())
    print('Email enviado com sucesso!')
except smtplib.SMTPException as e:
    print(f'Erro ao enviar email: {e}')

smtp.quit()
