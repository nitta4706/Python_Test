import smtplib, ssl
import base64
from email.mime.text import MIMEText



def mail_send(my_sender, email, my_pass):

 try:
  #登録するための固定アカウント内容
  account = "saikio4706@yahoo.co.jp"
  password = "nfgwe4706"
  from_email = "info@gay86.com"
  to_email = my_sender

  subject = "新規登録完了のお知らせ"
  my_data = "ご登録ありがとうございます\n\n"
  my_data = my_data + "下記の内容で新規登録完了しました。\n\n"
  my_data = my_data + "お客様のメールアドレス: " + email + "gay86.com\n"
  my_data = my_data + "お客様の登録パスワード: " + my_pass + "\n\n"
  my_data = my_data + "何かありましたら下記までご連絡下さい。\n\n"
  my_data = my_data + "****************************************\n"
  my_data = my_data + "株式会社 G\n"
  my_data = my_data + "メールアドレス:info@gay86.com\n"
  my_data = my_data + "電話番号:03-1111-1111\n"
  my_data = my_data + "****************************************\n"

  msg = MIMEText(my_data, "plain", "utf-8")
  msg.replace_header("Content-Transfer-Encoding", "base64")
  msg["Subject"] = subject
  msg["To"] = my_sender
  msg["From"] = from_email

  server = smtplib.SMTP("smtp.mail.yahoo.co.jp", 587)

  server.set_debuglevel(True)
  print('Saibi')
  server.login(account, password)
  server.sendmail(from_email, to_email, msg.as_string())
  server.quit()
  my_message = 'Send_OK'

 except Exception:
  error_flg = True
  my_message = 'Error'

 return my_message

