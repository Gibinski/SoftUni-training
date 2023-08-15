from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('<int:department_id>', details),
    path('template/<int:department_id>', details_template),
]
