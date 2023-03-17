from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.
def index(request):
	return render(request, "searchPage first page")

def logout_view(request):
	auth.logout(request)
	return redirect('home')