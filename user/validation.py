import re

def validate_email(email):
    regex_email = re.compile(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    )
    match = regex_email.match(email)
    return bool(match)

def validate_password(password):
    regex_password = re.compile(
        r'[a-zA-Z0-9`~!@#$%^&*()_+-={};:",./<>?]{8,25}'
    )
    match = regex_password.match(password)
    return bool(match)

def validate_mobile_number(mobile_number):
    regex_mobile_number = re.compile(
        r'^01[1|2|7|8|0|9]-?[0-9]{3,4}-?[0-9]{4}$'
    )
    match = regex_mobile_number.match(mobile_number)
    return bool(match)