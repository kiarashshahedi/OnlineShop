from kavenegar import *
from myshop.settings import Kavenegar_API
from random import randint
from zeep import Client


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




def send_otp_soap(mobile, otp):
    Clients = Client('https://api.kavenegar.com/soap/v1.asmx?wsdl')
    receptor = [mobile, ]

    emptyArrayPlaceholder = Clients.get_type('ns0:ArrayOfString')
    receptors = emptyArrayPlaceholder()
    for item in receptor:
        receptors['string'].append(item)


    api_key = KavenegarAPI(Kavenegar_API)
    message = 'your otp is {}'.format(otp)
    sender = '1000689696'
    status = 0
    statusMessage = ''
    result = Clients.service.SendSimpleByApikey(Kavenegar_API, sender, message, receptor, 0, 1, status, statusMessage)
    print(result)
    print(otp)



def get_random_otp():
    return print(randint(1000, 9999))
    
