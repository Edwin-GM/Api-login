from django.urls import path
from users import views


urlpatterns = [
    path('user/', views.users_view)
]