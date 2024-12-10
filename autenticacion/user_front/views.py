import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

BASE_API_URL = 'http://127.0.0.1:8000/'
# Create your views here.
def list_users(request):
    response = requests.get(f"{BASE_API_URL}user_api/users/")
    if response.status_code == 200:
        users = response.json()
        return render(request, 'user_front/list_users.html', {'users': users})
    else:
        return HttpResponse("Error")

def create_users(request):
    if request.method == 'POST':
        username = requests.post('username')
        email = requests.post('email')
        password = requests.post('password')
        
        user = User.objects.create_users(username=username, email=email, password=password)

    return render(request, 'user_front/create_user.html')

