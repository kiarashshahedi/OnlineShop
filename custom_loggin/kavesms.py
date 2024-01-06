from kavenegar import *
from myshop.settings import Kavenegar_API
from random import randint





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

def get_random_otp():
    return print(randint(1000, 9999))
    
