import json

from django.http import JsonResponse
from django.views import View

from posting.models import Posting

class PostingView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            Posting.objects.create(
            user = request.user,
            image_url = data['image_url'],
            text = data['text']
        )
        
        except KeyError:
            return JsonResponse({'message': KeyError}, status=400)

        except ValueError:
            return JsonResponse({'message': ValueError}, status=401)
    
