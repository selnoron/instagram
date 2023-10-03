from rest_framework import serializers
from main.models import MyUser


class UserSerializer(serializers.Serializer):
    email = serializers.CharField()
    nickname = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    avatar = serializers.ImageField()


class UserCreateSerializer(serializers.ModelSerializer):
    rate = serializers.FloatField(default=0)
    class Meta:
        model = MyUser
        fields = ['email', 
                  'nickname', 
                  'name', 
                  'description',
                  'avatar'
                ]



class FollowersSerializer(serializers.Serializer):
    follower = serializers.IntegerField()
    following = serializers.IntegerField()


class FollowersCreateSerializer(serializers.ModelSerializer):
    rate = serializers.FloatField(default=0)
    class Meta:
        model = MyUser
        fields = ['follower', 
                  'following'
                ]



class PublicationsSerializer(serializers.Serializer):
    p_type = serializers.CharField()
    author = serializers.IntegerField()
    file = serializers.FileField()


class PublicationsCreateSerializer(serializers.ModelSerializer):
    rate = serializers.FloatField(default=0)
    class Meta:
        model = MyUser
        fields = ['p_type', 
                  'author',
                  'file'
                ]
        


class LikesSerializer(serializers.Serializer):
    author = serializers.IntegerField()
    publication = serializers.IntegerField()


class LikesCreateSerializer(serializers.ModelSerializer):
    rate = serializers.FloatField(default=0)
    class Meta:
        model = MyUser
        fields = ['author', 
                  'publication'
                ]



class CommentSerializer(serializers.Serializer):
    author = serializers.IntegerField()
    publication = serializers.IntegerField()
    text = serializers.CharField()


class CommentCreateSerializer(serializers.ModelSerializer):
    rate = serializers.FloatField(default=0)
    class Meta:
        model = MyUser
        fields = ['author', 
                  'publication',
                  'text'
                ]



class ViewSerializer(serializers.Serializer):
    author = serializers.IntegerField()
    publication = serializers.IntegerField()


class ViewCreateSerializer(serializers.ModelSerializer):
    rate = serializers.FloatField(default=0)
    class Meta:
        model = MyUser
        fields = ['author', 
                  'publication'
                ]
