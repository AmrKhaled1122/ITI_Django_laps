from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
]
