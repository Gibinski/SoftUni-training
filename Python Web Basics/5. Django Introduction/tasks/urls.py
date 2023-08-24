from django.urls import path
from tasks.views import *

urlpatterns = [
    path('', index),
    path('list/', list_tasks),

]
