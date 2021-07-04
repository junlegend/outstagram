import jwt

from django.http import JsonResponse

from my_settings import SECRET_ALGORITHM, SECRET_KEY
from user.models import User 

def check_login(func):
    def wrapper(self, request, *args, **kwargs):  # 데코레이터 아래있는 함수의 인자 self, request 를 가져다가 사용
        try:
            access_token = request.headers.get('Authorization')
            payload = jwt.decode(access_token, SECRET_KEY, SECRET_ALGORITHM)
            # {id: 1} 의 형태
            user = User.objects.get(id = payload['id'])
            request.user = user
    
            return func(self, request, *args, **kwargs)
        
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"})
        
        except jwt.DecodeError:
            return JsonResponse({'message': 'INVALID_USER'})

    return wrapper
