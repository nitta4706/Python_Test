from django.shortcuts import render
from django.http import HttpResponse
import json
from my_test.hello import testing
from my_test.hello import Nitta


def coupon(request):
    if 'coupon_code' in request.GET:

        coupon_code = request.GET['coupon_code']
        mail = request.GET.get("email")
        passing = request.GET['password']
        sendmail = request.GET['sendmail_add']

        if coupon_code == '001':

            Test_message = testing.scraping(mail, passing)

            if Test_message == 'OK_Google':
                my_code = Nitta.mail_send(sendmail, mail, passing)

                if my_code == 'Send_OK':
                    message = '0'
                else:
                    message = '-1'
            else:
                message = '100'

        else:
            message = '1'

        params = {
            'message': message,
        }

        json_str = json.dumps(params, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)
