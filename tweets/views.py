import json
from django.views import View
from django.http import JsonResponse
from .models import Tweets

class Tweet(View):
    def post(self, request):
        data = json.loads(request.body)
        tweet = Tweets(name=data["name"],contents=data["contents"])
        tweet.save()
        return JsonResponse({"message": "SUCCESS"}, status=200)
   
    def get(self, request):
        tweet = list(Tweets.objects.values())
        return JsonResponse( tweet, safe=False, status=200)
      
