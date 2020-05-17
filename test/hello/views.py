from django.shortcuts import render
from django.http import HttpResponse
import json

def coupon(request):

    if 'coupon_code' in request.GET:

        coupon_code = request.GET['coupon_code']
        mail = request.GET.get("email")
        #passing = request.GET['password']
        #sendmail = request.GET['sendmail_add']


        if coupon_code == '001':
           message = '0'

        elif coupon_code == '002':
           message = '-1'

        else:
           message = '1'
	
        params = {
	   'message':message,
	   'mail':mail,
           #'passing':passing,
	   #'sendmail':sendmail
	}

        json_str=json.dumps( params, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)

