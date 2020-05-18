from django.shortcuts import render
from django.http import HttpResponse
import json
from my_test.hello import testing
from my_test.hello import Nitta

try:
    email = "saikio4706"
    password = "nfgwe4706"
    sendmail_add = "saikio4706@gmail.com"

    Test_message = testing.scraping(email, password)
    print(Test_message)

    if Test_message == 'OK_Google':

        my_code = Nitta.mail_send(sendmail_add, email, password)
        print(my_code)

        if my_code == 'Send_OK':
            message_num = '0'
        else:
            message_num = '-1'

    else:
        message_num = '-1'

except Exception:
    import traceback
    traceback.print_exc()
    error_flg = True
    message_num = '-1'

print(message_num)
