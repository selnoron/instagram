from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, filters
from rest_framework.request import Request
from rest_framework.response import Response
from main.models import MyUser, Followers, Publications, Likes, View, Comments
from main.serializer import (
    UserSerializer, 
    UserCreateSerializer, 
    FollowersSerializer, 
    FollowersCreateSerializer,
    PublicationsSerializer,
    PublicationsCreateSerializer,
    LikesSerializer,
    LikesCreateSerializer,
    CommentSerializer,
    CommentCreateSerializer,
    ViewSerializer,
    ViewCreateSerializer
    )
from rest_framework.validators import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import (
    IsAuthenticated
)

class UserViewSet(viewsets.ViewSet):
    queryset = MyUser.objects.all()
    permission_classes = [IsAuthenticated]


    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        filter_backends = [
            filters.SearchFilter,
        ]
        search_fields = ['=email']
        serializer: UserSerializer = UserSerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self,
        request: Request,
        pk: int = None
    ) -> Response:
        try:
            user = self.queryset.get(pk=pk)
        except MyUser.DoesNotExist:
            raise ValidationError('Object Does NOT exists', code=404)
        serializer = UserSerializer(
            instance=user
        )
        return Response(
            data=serializer.data
        )
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        serializer = UserCreateSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        user: MyUser = serializer.save()
        return Response(
            data={
                'status': 'ok',
                'message': \
                    f"Game {user.nickname} is created! ID: {user.pk}"
            }
        )
    
    def destroy(
        self,
        request: Request,
        pk = None,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        try:
            user = get_object_or_404(MyUser, pk=pk)
            user.delete()
            return Response(
                data={
                    'status':'ok',
                    'message':f'User {user.nickname} is deleted!'
                }
            )
        except user.DoesNotExist:
            raise ValidationError('User with such an ID does not exist',code=404)
        
    
class FollowersViewSet(viewsets.ViewSet):
    queryset = Followers.objects.all()
    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        serializer: FollowersSerializer = FollowersSerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self,
        request: Request,
        pk: int = None
    ) -> Response:
        try:
            followers = self.queryset.get(pk=pk)
        except Followers.DoesNotExist:
            raise ValidationError('Object Does NOT exists', code=404)
        serializer = FollowersSerializer(
            instance=followers
        )
        return Response(
            data=serializer.data
        )
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        serializer = FollowersCreateSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        followers: Followers = serializer.save()
        return Response(
            data={
                'status': 'ok',
                'message': \
                    f"Game {followers.nickname} is created! ID: {followers.pk}"
            }
        )
    
    def destroy(
        self,
        request: Request,
        pk = None,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        try:
            fol = get_object_or_404(Followers, pk=pk)
            fol.delete()
            return Response(
                data={
                    'status':'ok',
                    'message':f'{fol.follower} {fol.following} are not following now!'
                }
            )
        except fol.DoesNotExist:
            raise ValidationError('Followers with such an ID does not exist',code=404)
    

class PublicationViewSet(viewsets.ViewSet):
    queryset = Publications.objects.all()
    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        serializer: PublicationsSerializer = PublicationsSerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self,
        request: Request,
        pk: int = None
    ) -> Response:
        try:
            publication = self.queryset.get(pk=pk)
        except Publications.DoesNotExist:
            raise ValidationError('Object Does NOT exists', code=404)
        serializer = PublicationsSerializer(
            instance=publication
        )
        return Response(
            data=serializer.data
        )
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        serializer = PublicationsCreateSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        publication: Publications = serializer.save()
        return Response(
            data={
                'status': 'ok',
                'message': \
                    f"Game {publication.nickname} is created! ID: {publication.pk}"
            }
        )
    
    def destroy(
        self,
        request: Request,
        pk = None,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        try:
            pub = get_object_or_404(Publications, pk=pk)
            pub.delete()
            return Response(
                data={
                    'status':'ok',
                    'message':f'Publication is deleted!'
                }
            )
        except pub.DoesNotExist:
            raise ValidationError('Publication with such an ID does not exist',code=404)
    

class LikesViewSet(viewsets.ViewSet):
    queryset = Likes.objects.all()
    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        serializer: LikesSerializer = LikesSerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self,
        request: Request,
        pk: int = None
    ) -> Response:
        try:
            like = self.queryset.get(pk=pk)
        except Likes.DoesNotExist:
            raise ValidationError('Object Does NOT exists', code=404)
        serializer = LikesSerializer(
            instance=like
        )
        return Response(
            data=serializer.data
        )
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        serializer = LikesCreateSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        like: Likes = serializer.save()
        return Response(
            data={
                'status': 'ok',
                'message': \
                    f"Game {like.nickname} is created! ID: {like.pk}"
            }
        )
    
    def destroy(
        self,
        request: Request,
        pk = None,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        try:
            like = get_object_or_404(Likes, pk=pk)
            like.delete()
            return Response(
                data={
                    'status':'ok',
                    'message':f'Like is deleted!'
                }
            )
        except like.DoesNotExist:
            raise ValidationError('Like with such an ID does not exist',code=404)
    

class CommentViewSet(viewsets.ViewSet):
    queryset = Comments.objects.all()
    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        serializer: CommentSerializer = CommentSerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self,
        request: Request,
        pk: int = None
    ) -> Response:
        try:
            comment = self.queryset.get(pk=pk)
        except Comments.DoesNotExist:
            raise ValidationError('Object Does NOT exists', code=404)
        serializer = LikesSerializer(
            instance=comment
        )
        return Response(
            data=serializer.data
        )
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        serializer = CommentCreateSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        comment: Comments = serializer.save()
        return Response(
            data={
                'status': 'ok',
                'message': \
                    f"Game {comment.nickname} is created! ID: {comment.pk}"
            }
        )
    
    def destroy(
        self,
        request: Request,
        pk = None,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        try:
            comment = get_object_or_404(Comments, pk=pk)
            comment.delete()
            return Response(
                data={
                    'status':'ok',
                    'message':f'Comment is deleted!'
                }
            )
        except comment.DoesNotExist:
            raise ValidationError('Comment with such an ID does not exist',code=404)
    

class ViewViewSet(viewsets.ViewSet):
    queryset = View.objects.all()
    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        serializer: ViewSerializer = ViewSerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self,
        request: Request,
        pk: int = None
    ) -> Response:
        try:
            view = self.queryset.get(pk=pk)
        except View.DoesNotExist:
            raise ValidationError('Object Does NOT exists', code=404)
        serializer = ViewSerializer(
            instance=view
        )
        return Response(
            data=serializer.data
        )
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        serializer = ViewCreateSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        view: View = serializer.save()
        return Response(
            data={
                'status': 'ok',
                'message': \
                    f"Game {view.nickname} is created! ID: {view.pk}"
            }
        )
    

class UserFilterSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'nickname']
    search_fields = ['^email', '^nickname', '^description']
    ordering_fields = ['nickname', 'id']
    ordering = ['id']

class PublicationsFilterSet(viewsets.ModelViewSet):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'author']
    search_fields = ['^text', '^author']
    ordering_fields = ['nickname', 'id']
    ordering = ['id']
