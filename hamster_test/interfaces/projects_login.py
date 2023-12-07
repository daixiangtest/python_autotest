import time

import requests


class Projects:
    token = "Bearer "

    def __init__(self):
        response = requests.request("POST", "https://computeshare-frontend.hamster.newtouch.com/api/v1/sms/send",
                                    headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                    data='countryCallCoding=%2B86&telephoneNumber=18326447662')

        print(response.text)
        response = requests.request("POST", "https://computeshare.hamster.newtouch.com/v1/user/login_by_vc",
                                    headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                    data='countryCallCoding=%2B86&telephoneNumber=18326447662&validateCode=000000')
        print(response.text)
        self.token += response.json()["data"]["token"]

    @staticmethod
    def test_send():
        response = requests.request("POST", "https://computeshare-frontend.hamster.newtouch.com/api/v1/sms/send",
                                    headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                    data='countryCallCoding=%2B86&telephoneNumber=18326447662')
        return response.json()

    @staticmethod
    def test_login_by_vc():
        response = requests.request("POST", "https://computeshare.hamster.newtouch.com/v1/user/login_by_vc",
                                    headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                    data='countryCallCoding=%2B86&telephoneNumber=18326447662&validateCode=000000')
        return response.json()


if __name__ == '__main__':
    p = Projects()
    print(p.token)
    A = Projects.test_send()
    B = Projects.test_login_by_vc()
    print(B, A)
