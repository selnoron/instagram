from django.shortcuts import render
from django.views.generic import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet
from main.models import MyUser, MyUserManager
from rest_framework.validators import ValidationError

class AuthView(View):
    querylist = MyUser.objects.all()

    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'auth.html'
        return render(
            request=request,
            template_name=template_name,
            context={
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'main.html'
        data = request.POST
        try:
            user = self.queryset.get(email=data.get("email"))
            request.session["user"] = user
            return render(
                request=request,
                template_name=template_name,
                context={
                    "user": user
                }
            )
        except MyUser.DoesNotExist:
            raise ValidationError('Object Does NOT exists', code=404)
        
class RegisView(View):
    querylist = MyUser.objects.all()

    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'regis.html'
        return render(
            request=request,
            template_name=template_name,
            context={
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'auth.html'
        data = request.POST
        try:
            if data.get('password') == data.get('repeat_password'):
                MyUser.objects.create_user(
                    email=data.get("email"),
                    nickname=data.get("nickname"),
                    password=data.get("password"),
                )
            return render(
                request=request,
                template_name=template_name,
                context={
                }
            )
        except MyUser.DoesNotExist:
            raise ValidationError('Object Does NOT exists', code=404)
