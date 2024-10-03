from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def get_isvibra(request):
    global isvibra
    if request.GET.get('vibra'):
        if request.GET.get('vibra') == '1':
            isvibra = True
        else:
            isvibra = False
        return JsonResponse({'isvibra': isvibra})
    else:
        return JsonResponse({'isvibra': isvibra})