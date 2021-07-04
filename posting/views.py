import json

from django.http import JsonResponse
from django.views import View

from .models import Posting
from user.utils import check_login

class PostingView(View):
    @check_login
    def post(self, request):
        data = json.loads(request.body)
        try:
            Posting.objects.create(
                user = request.user,
                image_url = data['image_url'],
                text = data['text']
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
    
    def get(self, request):
        postings = Posting.objects.all()
        results = []

        for posting in postings:
            results.append({
                "posting_id": posting.id,
                "posting_user": posting.user.name,
                "image_url": posting.image_url,
                "text": posting.text,
                "created_at": posting.created_at
            })
        
        return JsonResponse({"results": results}, status=200)



