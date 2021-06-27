import json

from django.http  import JsonResponse
from django.views import View

from .models      import User
from .validation   import *


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

            User.objects.create(
                name = data['name'],
                email = data['email'],
                password = data['password'],
                mobile_number = data['mobile_number'],
                nickname = data['nickname']
            )
            
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        
        #except KeyError:
            #return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except Exception as error:
            print(error.__class__)
            return JsonResponse({'message': 'ERROR'})
