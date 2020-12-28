from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import SimpleTemplateResponse, Response
from django.contrib.auth import authenticate, login
from rest_framework.serializers import ModelSerializer


from .forms import (LoginForm)


class LoginView(APIView):

    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form,
            'check': "am"
        }
        return render(request,
                      'account/login.html',
                      context)

    def post(self, request):
        login_form = LoginForm(data=request.data)
        context = {}
        if login_form.is_valid():
            auth_user = authenticate(mobile=request.data['mobile'],
                                     password=request.data['password'])
            if auth_user:
                login(request, auth_user)
                serialized_data = ModelSerializer(auth_user, many=True)
                context = serialized_data
            else:
                context = {
                    'mistake': 'Username/Password is wrong'
                }
        else:
            context = login_form.errors
        return SimpleTemplateResponse('account/profile.html',
                                      context)
