from django.urls import path
from .views import EmployeesView

urlpatterns = [
    path('employees/', EmployeesView.as_view(), name='employees'),
    path('employees/<str:username>/', EmployeesView.as_view(), name='employee_detail'),
]