import jwt, json

from django.http import JsonResponse
from .models import Users

def login_required(func):

   def wrapper(self, request, *args, **kwargs):
      # access_token = request.headers.get('Authorization', None)
       access_token = request.COOKIES.get('jwt', None)
       secret = 'secret_is_secret'
       if access_token:
           try:
               decode = jwt.decode(access_token, secret, algorithms=['HS256'])
               user_id = decode["user_id"]
               user = Users.objects.get(id=user_id)
               request.user = user
           except jwt.DecodeError:
               return JsonResponse({"error_code" : "INVALID_TOKEN"},status = 401)
           except Users.DoesNotExist:
               return JsonResponse({"message" : "존재하지 않는 아이디 입니다.", "error_code" : "USER_NOT_FOUND"}, status=401)

           return func(self, request, *args, **kwargs)
       else:
           return JsonResponse({"message" : "로그인이 필요한 서비스 입니다." , "error_code":"NEED_LOGIN"},status=401)
   return wrapper
