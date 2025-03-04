from django.shortcuts import render, get_list_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def user_list(request):
    if request.method == "GET":
        users = list(User.objects.values())
        return JsonResponse(users, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.create_user(username=data["username"], password=data["password"])
        return JsonResponse({"id": user.id, "username": user.username})
    

@csrf_exempt
def user_detali(request, id):
    user = get_list_or_404(User, id=id) 
    return JsonResponse({"id": user.id, "username": user.username})   