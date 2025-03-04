from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Reservation
from tables.models import Table
from django.contrib.auth.models import User

@csrf_exempt
def create_reservation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = get_object_or_404(User, id=data["user_id"])
        table = get_object_or_404(Table, id=data["table_id"])
        existing_reservation = Reservation.objects.filter(user=user, data=data["date"]).exists()
        if existing_reservation:
            return JsonResponse({"error": "User already has a reservation on this date"}, status=400)
        

        reservation = Reservation.objects.create(user=user, table=table, date=data["date"], status="pending")
        return JsonResponse ({"id": reservation.id, "status": reservation.status})
    
