from django.shortcuts import render

def index(request):
    return render(request, 'ProfApp/index.html')

def before(request):
    return render(request, 'ProfApp/class_management_before.html')

def ing(request):
    return render(request, 'ProfApp/class_management_ing.html')

def after(request):
    return render(request, 'ProfApp/class_management_after.html')