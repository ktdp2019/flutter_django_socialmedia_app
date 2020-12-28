from django.urls import path
from .views import (LoginView)

app_name = 'account'

urlpatterns = [
    path('', LoginView.as_view(), name='login')
]
