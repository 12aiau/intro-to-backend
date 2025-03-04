from django.urls import path
from .views import user_list, user_detali

urlpatterns = [
    path("users/", user_list),
    path("users/<int:id>/", user_detali),

]