import requests
from requests.auth import HTTPDigestAuth

url = 'https://httpbin.org/digest-auth/auth/user/pass'

#username is user
#password is pass


responce = requests.get(url, auth=HTTPDigestAuth('user', 'pass'))

if responce.status_code == 200:

    print('Request Code Status is {}\n Login Sucesss '.format(responce.status_code))

else:
    print("Check Passcode")
