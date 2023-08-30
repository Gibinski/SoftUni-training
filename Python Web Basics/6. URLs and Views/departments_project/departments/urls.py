from django.urls import path
from .views import details, details_template, index, details_error

urlpatterns = [
    path('', index, name='index page'),
    path('int/<int:department_id>', details, name='departments int'),
    path('template/<int:department_id>', details_template, name='departments template'),
    path('error/', details_error, name='departments error'),
    path('<department_id>', details, name='departments only id'),
]
