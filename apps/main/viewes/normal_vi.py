from django.shortcuts import (
    render, 
    redirect
)
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
    Comments,
    Followers
)
from rest_framework.validators import ValidationError
from django.db import IntegrityError
from main.serializer import (
    UserSerializer,
    PublicationsSerializer,
    HistorySerializer,
    CommentSerializer,
    FollowersSerializer
)
from django.core.files.uploadedfile import InMemoryUploadedFile
import uuid


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
        files: dict = request.FILES

        main_image: InMemoryUploadedFile = None
        print(files)
        if files != {}:
            main_image = files.get('avatar')
            main_image.name = f'{uuid.uuid1()}.png'
        else:
            main_image = 'avatars/unknown.png'
        print(main_image)
        try:
            if data.get('password') == data.get('repeat_password'):
                MyUser.objects.create_user(
                    email=data.get("email"),
                    nickname=data.get("nickname"),
                    name=data.get("name"),
                    description=data.get("description"),
                    avatar=main_image,
                    password=data.get("password")
                )
                return redirect('/auth/')
            else:
                return redirect("/")
        except MyUser.DoesNotExist:
            raise ValidationError('Object Does NOT exists', code=404)


class ProfView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        if 'user' not in request.session.keys():
            return redirect('/auth/')
        template_name: str = 'profile.html'
        user: MyUser = MyUser.objects.get(pk=pk)
        likes: list[int] = \
            [len(Likes.objects.filter(publication=post)) for post in user.posts.all()]
        l_posts: int = len(user.posts.all())
        posts: list[dict] = []
        for i in range(len(user.posts.all())):
            dat = PublicationsSerializer(instance=user.posts.all()[i]).data
            dat["likes"] = likes[i]
            posts.append(dat)
        fol: Followers = Followers.objects.filter(follower=user)
        l_fol: int = len(fol)
        fow: Followers = Followers.objects.filter(following=user)
        l_fow: int = len(fow)
        user = UserSerializer(
            instance=user
        ).data
        return render(
            request=request,
            template_name=template_name,
            context={
                'user': user,
                'posts': posts,
                'lposts': l_posts,
                'lfol': l_fol,
                'lfow': l_fow,
                'session': request.session['user'].get("nickname")
            }
        )


class MainView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if 'user' not in request.session.keys():
            return redirect('/auth/')
        template_name: str = 'main.html'
        user_s: dict = request.session["user"]
        user: MyUser = MyUser.objects.get(email=user_s.get("email"))
        fol: Followers = Followers.objects.filter(follower=user)
        fols: Followers = []
        for i in range(len(fol)):
            fols.append(FollowersSerializer(instance=fol[i]).data)


        pos: Publications = Publications.objects.all()
        likes: list[int] = \
            [len(Likes.objects.filter(publication=post)) for post in pos]
        posts: list[dict] = []
        u_his = user.histories.all()
        for i in range(len(pos) - 1, -1, -1):
            dat = PublicationsSerializer(instance=pos[i]).data
            dat["likes"] = likes[i]
            posts.append(dat)
        his: History = []
        for i in u_his:
            h = HistorySerializer(
                    instance=i
                ).data
            if h.get("file")[-3:] == "mp4":
                h['format'] = "mp4"
            else:
                h['format'] = "png"
            his.append(h)
        for i in range(len(fols)):
            a = History.objects.filter(
                    author=MyUser.objects.get(email=fols[i].get("following").get("email"))
            )
            print(a)
            if a:
                for j in a:
                    y = HistorySerializer(j).data
                    if y.get("file")[-3:] == "mp4":
                        y['format'] = "mp4"
                    else:
                        y['format'] = "png"
                    his.append(y)
            else:
                continue
            
        hiss = his
        user = UserSerializer(
            instance=user
        ).data
        print(hiss)
        return render(
            request=request,
            template_name=template_name,
            context={
                'user': user,
                'posts': posts,
                'hiss': hiss
            }
        )


class LikeView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        if 'user' not in request.session.keys():
            return redirect('/auth/')
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
        if 'user' not in request.session.keys():
            return redirect('/auth/')
        template_name: str = 'his.html'
        his = HistorySerializer(History.objects.get(pk=pk)).data
        if his.get("file")[-3:] == "mp4":
            his['format'] = "mp4"
        else:
            his['format'] = "png"
        return render(
            request=request,
            template_name=template_name,
            context={
                'his': his
            }
        )
    

class ComView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        if 'user' not in request.session.keys():
            return redirect('/auth/')
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
    

class ListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if 'user' not in request.session.keys():
            return redirect('/auth/')
        template_name: str = 'list_users.html'
        current_user: MyUser = MyUser.objects.get(email=request.session["user"].get("email"))
        subscribed_users = Followers.objects.filter(follower=current_user).values_list('following', flat=True)
        user = MyUser.objects.exclude(id__in=subscribed_users)    
        users: list = \
            [UserSerializer(instance=us).data for us in user]
        return render(
            request=request,
            template_name=template_name,
            context={
                "users": users
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        user = MyUser.objects.get(nickname=request.POST.get('nickname'))
        user_s = UserSerializer(user).data
        try:
            Followers.objects.create(
                follower=MyUser.objects.get(email=request.session['user'].get("email")),
                following=user
            )
            return redirect(f'/inst/us/list/')
        except:
            return HttpResponse("ERROR")


class MkHisView(View):
    querylist = MyUser.objects.all()

    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'make_his.html'
        if 'user' not in request.session.keys():
            return redirect('/inst/')
        return render(
            request=request,
            template_name=template_name,
            context={
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        data = request.POST
        files: dict = request.FILES
        user: MyUser = MyUser.objects.get(email=request.session["user"].get("email"))
        main_file: InMemoryUploadedFile = None
        print(files)
        if files != {}:
            main_file = files.get('file')
            print(main_file.name[-3:])
            if main_file.name[-3:] == "mp4":
                main_file.name = f'{uuid.uuid1()}.mp4'
            else:
                main_file.name = f'{uuid.uuid1()}.png'
        else:
            return HttpResponse("ERROR")

        History.objects.create(
            author=user,
            file=main_file
        )
        return redirect('/inst/')

class MkPosView(View):
    querylist = MyUser.objects.all()

    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'make_pub.html'
        if 'user' not in request.session.keys():
            return redirect('/inst/')
        return render(
            request=request,
            template_name=template_name,
            context={
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        data = request.POST
        files: dict = request.FILES

        main_image: InMemoryUploadedFile = None
        if files != {}:
            main_image = files.get('file')
            main_image.name = f'{uuid.uuid1()}.png'
        try:
            Publications.objects.create(
                p_type=data.get("ty"),
                author=MyUser.objects.get(email=request.session["user"].get("email")),
                file=main_image
            )
            return redirect('/inst/')
        except MyUser.DoesNotExist:
            raise ValidationError('Object Does NOT exists', code=404)