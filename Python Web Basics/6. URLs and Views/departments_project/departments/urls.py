from django.urls import path
from .views import details, details_template, index

urlpatterns = [
    path('', index),
    path('int/<int:department_id>', details),
    path('template/<int:department_id>', details_template),
    path('<department_id>', details),
]
