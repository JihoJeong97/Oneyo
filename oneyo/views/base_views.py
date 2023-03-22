from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("검색 페이지")

from django.shortcuts import render

def index(request):
    return render(request, 'base.html')
