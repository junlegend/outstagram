import bcrypt
import json
import jwt

from django.http  import JsonResponse
from django.views import View

from user.models     import User
from my_settings     import SECRET_KEY, SECRET_ALGORITHM
from user.validation import validate_email, validate_password, validate_mobile_number

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            if not validate_email(data['email']):
                raise ValueError
            
            if not validate_password(data['password']):
                raise ValueError

            if not validate_mobile_number(data['mobile_number']):
                raise ValueError
            
            password         = data['password']
            encoded_password = password.encode('utf-8')
            hashed_password  = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

            User.objects.create(
                name          = data['name'],
                email         = data['email'],
                password      = hashed_password.decode('utf-8'),
                mobile_number = data['mobile_number'],
                nickname      = data['nickname']
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message': KeyError}, status=400)
        
        except ValueError:
            return JsonResponse({'message': ValueError}, status=401)


class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        user     = User.objects.get(email = data['email'])
        password = data['password']
        
        encoded_password = password.encode('utf-8')
        check_password   = bcrypt.checkpw(encoded_password, user.password.encode('utf-8'))
        
        access_token = jwt.encode({'id': user.id}, SECRET_KEY, SECRET_ALGORITHM)

        try:
            if user and check_password:
                return JsonResponse({'message': 'SUCCESS', 'access_token': access_token}, status=200)
        
        except KeyError:
            return JsonResponse({'message': KeyError}, status=400)
        
        except ValueError:
            return JsonResponse({'message': ValueError}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'message': User.DoesNotExist}, status=401)

