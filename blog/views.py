from django.shortcuts import render
from django.http import JsonResponse



def return_Jason(request):
    return JsonResponse({
        'type':'buttons',
        'buttons':['option1','option2','option3']
    })
