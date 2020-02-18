import json
import bcrypt
import jwt
from django.views import View
from django.http  import HttpResponse, JsonResponse
from .models      import Users
from .utils       import login_required

class SignUpView(View):

    def post(self,request):
        data = json.loads(request.body)
        
        if Users.objects.filter(email=data['email']).exists():
            return JsonResponse({"message":"EMAIL_EXIST"}, status=400)
        else:
            password = bytes(data["password"], "utf-8")
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            
            new_user = Users(
                name = data["name"],
                password = hashed_password.decode("utf-8"),
                email = data["email"],
            )
            new_user.save()
            
            return JsonResponse({"message":"SUCCESS"}, status=200)
 
class AuthView(View):

    def post(self,request):
        login_user = json.loads(request.body)
        secret = 'secret_is_secret'

        if Users.objects.filter(email = login_user["email"]).exists():
            user_data = Users.objects.get(email=login_user["email"])
        else:
            return JsonResponse(
                {
                    "message" : "EMAIL_NOT_FOUND"
                },status=400
            )
        
        if bcrypt.checkpw(login_user["password"].encode("utf-8"), user_data.password.encode("utf-8")):
            encoded_jwt = jwt.encode({"user_id":user_data.id}, secret, algorithm="HS256")
            response = HttpResponse(status = 200)
            response.set_cookie('jwt', encoded_jwt.decode('utf-8'), httponly=True, max_age = None)
            print(response)
            return response
        else:
            return JsonResponse(
                { 
                    "message" : "WRONG_PASSWORD" 
                }, status=400
            )

class UserView(View):
    @login_required
    def get(self, request):
        user = Users.objects.filter(id = request.user.id).values()
        return JsonResponse({'data' : user[0]}, status = 200)
