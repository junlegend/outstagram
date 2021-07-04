import re

def validate_email(email):
    #regex_email = re.compile(
    #    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    #)
    #match = regex_email.match(email)
    #return match
    result = re.match(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        email
    )
    return result


def validate_password(password):
    #regex_password = re.compile(
    #    r'[a-zA-Z0-9`~!@#$%^&*()_+-={};:",./<>?]{8,25}'
    #)
    #match = regex_password.match(password)
    #return match
    result = re.match(
        r'[a-zA-Z0-9`~!@#$%^&*()_+-={};:",./<>?]{8,25}',
        password
    )
    return result


def validate_mobile_number(mobile_number):
    #regex_mobile_number = re.compile(
    #    r'^01[1|2|7|8|0|9]-?[0-9]{3,4}-?[0-9]{4}$'
    #)
    #match = regex_mobile_number.match(mobile_number)
    #return match
    result = re.match(
        r'^01[0|1|2|7|8|9]-?[0-9]{3,4}-?[0-9]{4}$',
        mobile_number
    )
    return result