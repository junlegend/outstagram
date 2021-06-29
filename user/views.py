import bcrypt
import json
import jwt

from django.http  import JsonResponse
from django.views import View

from .models      import User
from my_settings  import SECRET_KEY
from .validation  import *


class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not validate_password(data['password']):
                return JsonResponse({'message': 'More than 8 characters needed'}, status=400)

            if not validate_email(data['email']):
                return JsonResponse({'message': 'Must contain @ and .'}, status=400)

            if not validate_mobile_number(data['mobile_number']):
                return JsonResponse({'message':'Correct form: 010-(0)000-0000'}, status=400)           
            
            if User.objects.filter(name=data['name']).exists():
                return JsonResponse({'message': 'Already registered name'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'Already registered email'}, status=400)
            
            if User.objects.filter(mobile_number=data['mobile_number']).exists():
                return JsonResponse({'message': 'Already registered mobile_number'}, status=400)
            
            encoded_password = data['password'].encode('utf-8')
            hashed_password  = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

            User.objects.create(
                name          = data['name'],
                email         = data['email'],
                password      = hashed_password.decode('utf-8'),
                mobile_number = data['mobile_number'],
                nickname      = data['nickname']
            )
            
            email = User.objects.get(email=data['email'])
            SECRET = SECRET_KEY
            token = jwt.encode({'id': email.id}, SECRET, algorithm='HS256')
            return JsonResponse({'message': 'SUCCESS', 'token': token}, status=201)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)


class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            email            = User.objects.get(email=data['email'])
            encoded_password = data['password'].encode('utf-8')
            
            SECRET = SECRET_KEY
            token  = jwt.encode({'id': email.id}, SECRET, algorithm='HS256')

            if bcrypt.checkpw(encoded_password, email.password.encode('utf-8')):
                return JsonResponse({'message': 'S', 'token': token}, status=201)
            
            else:
                return JsonResponse({'message': 'I'}, status=401)
                
        except KeyError:
            return JsonResponse({'message': 'K'}, status=400)
            
        except User.DoesNotExist:
            return JsonResponse({'message': 'I'}, status=401)
