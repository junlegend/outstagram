import re

def valdate_email(email):
    result = re.match(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        email
    )
    return result

def validate_password(password):
    result = re.match(
        r'[a-zA-Z0-9`~!@#$%^&*()_+-={};:",./<>?]{8,25}',
        password
    )
    return result

def validate_mobile_number(mobile_number):
    result = re.match(
        r'^01[0|1|2|7|8|9]-?[0-9]{3,4}-?[0-9]{4}$',
        mobile_number
    )
    return result
