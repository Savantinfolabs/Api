from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def Amount(request):
    return JsonResponse({'Amount': '10000'})