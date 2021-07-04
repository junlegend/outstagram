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
            if not validate_password(data['password']):
                raise ValueError
            
            if not validate_email(data['email']):
                raise ValueError

            if not validate_mobile_number(data['mobile_number']):
                raise ValueError

            #if User.objects.filter(name=data['name']).exists():
            #    return JsonResponse({'message': 'Already registered name'}, status=400)
            #if User.objects.filter(email=data['email']).exists():
            #    return JsonResponse({'message': 'Already registered email'}, status=400)
            #
            #if User.objects.filter(mobile_number=data['mobile_number']).exists():
            #    return JsonResponse({'message': 'Already registered mobile_number'}, status=400)

            encoded_password = data['password'].encode('utf-8')
            hashed_password  = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            
            user = User.objects.create(
                name          = data['name'],
                email         = data['email'],
                password      = hashed_password.decode('utf-8'),
                # models.py 에서 password 컬럼의 타입을 CharField 로 지정했으므로  
                # database 에 저장할 때는 디코드한 string 형태로 저장 
                mobile_number = data['mobile_number'],
                nickname      = data['nickname']
            )
            
            access_token = jwt.encode({'id': user.id}, SECRET_KEY, SECRET_ALGORITHM)
            
            return JsonResponse({'message': 'SUCCESS', 'access_token': access_token}, status=201)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
            # Bad request > status code = 400

        except ValueError:
            return JsonResponse({'message': 'VALIDATION_ERROR'}, status=401)
            # Unauthorized > status code = 401

class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        user     = User.objects.get(email = data['email'])
        password = data['password']

        encoded_password = password.encode('utf-8')
        check_password   = bcrypt.checkpw(encoded_password, user.password.encode('utf-8'))

        access_token = jwt.encode({'id': user.id}, SECRET_KEY, SECRET_ALGORITHM)

        try:
            if check_password:
                return JsonResponse({'message': 'SUCCESS', 'access_token': access_token}, status=200)

        #try:
        #    user            = User.objects.get(email=data['email'])
        #    encoded_password = data['password'].encode('utf-8')
        #    access_token  = jwt.encode({'id': user.id}, SECRET_KEY, algorithm='HS256')
#
        #    if bcrypt.checkpw(encoded_password, user.password.encode('utf-8')):
        #        return JsonResponse({'message': 'S', 'access_token': access_token}, status=201)
        #    
        #    else:
        #        return JsonResponse({'message': 'INVALID_USER'}, status=401)
                
        except KeyError:
            return JsonResponse({'message': KeyError}, status=400)

        except ValueError:
            return JsonResponse({'message': ValueError}, status=401)
            # 입력한 password 가 id 에 매칭되는 password 가 아닐 때    
        
        except User.DoesNotExist:
            return JsonResponse({'message': User.DoesNotExist}, status=401)
            # 입력한 email 이 database 에 등록된 email 이 아닐 때