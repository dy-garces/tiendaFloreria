from django.shortcuts import render

# Create your views here.

def orden(request):
    return render(request, 'ordenes/orden.html')