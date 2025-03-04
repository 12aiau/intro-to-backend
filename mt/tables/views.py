from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Table

@csrf_exempt
def table_list(request):
    if request.method == "GET":
        tables = list(Table.objects.values())
        return JsonResponse(tables, safe=False)
    

@csrf_exempt
def create_table(request):
    if request.method == "POST":
        date = json.loads(request.body)
        table = Table.objects.create(number=date["number"], seats=date["seats"], is_available=True)
        return JsonResponse({"id": table.id, "number": table.number,"seats": table.seats, "is_available": table.is_available})
    



