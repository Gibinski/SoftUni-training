from django.shortcuts import render
from django.http import HttpResponse

def index(request):  
    return HttpResponse('index')


def details(request, department_id):
    print(department_id)
    
    department_map = {
        '1': "Developers",
        '2': "QA"
    }

    payload = f"Department: {department_map.get(str(department_id), 'Unknown')}"
    return HttpResponse(payload)


def details_template(request, department_id):
    department_map = {
        '1': "Developers",
        '2': "QA"
    }

    payload = f"Department: {department_map.get(str(department_id), 'Unknown')}"
    return render(request, 'departments/details.html')