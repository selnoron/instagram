from django.shortcuts import render, redirect
from django.views.generic import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet
from main.models import (
    MyUser, 
    MyUserManager, 
    Publications, 
    Likes,
    History,
    Comments
)
from rest_framework.validators import ValidationError
from django.db import IntegrityError
from main.serializer import (
    UserSerializer,
    PublicationsSerializer,
    HistorySerializer,
    CommentSerializer
)

class AuthView(View):
    querylist: MyUser = MyUser.objects.all()

    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'auth.html'
        if 'user' in request.session.keys():
            return redirect('/inst/')
        return render(
            request=request,
            template_name=template_name,
            context={
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        data = request.POST
        try:
            user: MyUser = self.querylist.get(email=data.get("email"))
            serializer = UserSerializer(
                instance=user
            )
            user = serializer.data

            request.session["user"] = {
                "email": user.get("email"),
                "name": user.get("name"),
                "description": user.get("description"),
                "avatar": user.get("avatar"),
                "nickname": user.get("nickname")
            }
            request.session.modified = True
            return redirect('/inst/')
        except MyUser.DoesNotExist:
            raise ValidationError('Object Does NOT exists', code=404)
        
class RegisView(View):
    querylist = MyUser.objects.all()

    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'regis.html'
        if 'user' in request.session.keys():
            return redirect('/inst/')
        return render(
            request=request,
            template_name=template_name,
            context={
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        data = request.POST
        print(data)
        try:
            if data.get('password') == data.get('repeat_password'):
                MyUser.objects.create_user(
                    email=data.get("email"),
                    nickname=data.get("nickname"),
                    name=data.get("name"),
                    description=data.get("description"),
                    avatar=data.get("avatar"),
                    password=data.get("password")
                )
            return redirect('/auth/')
        except MyUser.DoesNotExist:
            raise ValidationError('Object Does NOT exists', code=404)


class ProfView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'main.html'
        user_s: dict = request.session["user"]
        user: MyUser = MyUser.objects.get(email=user_s.get("email"))
        likes: list[int] = \
            [len(Likes.objects.filter(publication=post)) for post in user.posts.all()]
        posts: list[dict] = []
        for i in range(len(user.posts.all())):
            dat = PublicationsSerializer(instance=user.posts.all()[i]).data
            dat["likes"] = likes[i]
            posts.append(dat)
            print(PublicationsSerializer(instance=user.posts.all()[i]).data)
        return render(
            request=request,
            template_name=template_name,
            context={
                'user': user_s,
                'posts': posts
            }
        )


class MainView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'main.html'
        user_s: dict = request.session["user"]
        user: MyUser = MyUser.objects.get(email=user_s.get("email"))
        pos: Publications = Publications.objects.all()
        likes: list[int] = \
            [len(Likes.objects.filter(publication=post)) for post in pos]
        posts: list[dict] = []
        for i in range(len(pos) - 1, -1, -1):
            dat = PublicationsSerializer(instance=pos[i]).data
            dat["likes"] = likes[i]
            posts.append(dat)
        his: History = History.objects.all()
        hiss = [HistorySerializer(his[i]).data for i in range(len(his))]
        print(hiss)
        return render(
            request=request,
            template_name=template_name,
            context={
                'user': user_s,
                'posts': posts,
                'hiss': hiss
            }
        )


class LikeView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        try:
            Likes.objects.create(
                author=\
                    MyUser.objects.get(
                        email=request.session['user'].get("email")
                    ),
                publication=Publications.objects.get(pk=pk)
            )
            return redirect(f'/inst/')
        except IntegrityError:
            return HttpResponse(
                "<center>You already liked that post</center>"
            )
        

class HisView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        template_name: str = 'his.html'
        his = HistorySerializer(History.objects.get(pk=pk)).data
        return render(
            request=request,
            template_name=template_name,
            context={
                'his': his
            }
        )
    

class ComView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        template_name: str = 'com.html'
        post = Publications.objects.get(pk=pk)
        com = post.cpost.all()
        coms = []
        for i in range(len(com)):
            coms.append(
                CommentSerializer(
                    instance=com[i]
                ).data
            )
        print(coms)
        return render(
            request=request,
            template_name=template_name,
            context={
                "coms": coms
            }
        )
    
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        template_name: str = 'com.html'
        post = Publications.objects.get(pk=pk)
        com = post.cpost.all()
        Comments.objects.create(
            author=MyUser.objects.get(
                    email=request.session['user'].get("email")
                ),
            publication=post,
            text=request.POST.get('text')
        )
        return redirect(f'/inst/post/{pk}/comm')
    

class DisView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        del request.session['user']
        return redirect('/auth/')
    