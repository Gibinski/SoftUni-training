from django.http import HttpResponse

def index(request):  
    return HttpResponse('index')


def details(request, department_id):
    print(department_id)
    
    return HttpResponse('details')