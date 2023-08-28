from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):  
    return HttpResponse('index')

def details(request, department_id):
    department_map = {
        '1': "Developers",
        '2': "QA"
    }
    payload = f"Department: {department_map.get(str(department_id), 'Unknown')}"
    # return HttpResponse(payload)
    # return redirect('/departments/template', department_id=department_id)
    # return redirect('https://www.google.bg/')
    return redirect('departments template')

def details_template(request, department_id):
    print(department_id)
    print("department_id")
    department_map = {
        '1': "Developers",
        '2': "QA"
    }
    payload = f"Department: {department_map.get(str(department_id), 'Unknown')}"
    context = {
        "title": "Departments title from context",
        "payload": payload
    }

    return render(request, 'departments/details.html', context=context)
