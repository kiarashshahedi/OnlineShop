from kavenegar import *
from myshop.settings import Kavenegar_API
from random import randint
from zeep import Client
from . import models
import datetime
import time
from background_task import background




def send_otp(mobile, otp):
    mobile = [mobile, ]
    try:
        api = KavenegarAPI(Kavenegar_API)
        params = { 
            'sender' : '1000689696', 
            'receptor': mobile, 
            'message' : 'your otp is {}'.format(otp),
         }
        response = api.sms_send( params)
        print("OTP: ", otp)
        print(response)
    except APIException as e :
        print(e)
    except HTTPException as e :
        print(e)




@background(schedule=10)
def send_otp_soap(mobile, otp):

    time.sleep(10)
    client = Client('http://api.kavenegar.com/soap/v1.asmx?wsdl')
    receptor = [mobile, ]

    empty_array_placeholder = client.get_type('ns0:ArrayOfString')
    receptors = empty_array_placeholder()
    for item in receptor:
        receptors['string'].append(item)

    api_key = Kavenegar_API
    message = 'Your OTP is {}'.format(otp)
    sender = '1000596446'
    status = 0
    status_message = ''

    result = client.service.SendSimpleByApikey(api_key,
                                               sender,
                                               message,
                                               receptors,
                                               0,
                                               1,
                                               status,
                                               status_message)
    print(result)
    print('OTP: ', otp)


def get_random_otp():
    otp = randint(1000, 9999)
    return otp
    
def check_otp_expiration(mobile):
    try:
        user = models.MyUser.objects.get(mobile=mobile)
        now = datetime.datetime.now()
        otp_time = user.otp_create_time
        diff_time = now - otp_time
        print('OTP TIME: ', diff_time)

        if diff_time.seconds > 120:
            return False
        return True

    except models.MyUser.DoesNotExist:
        return False