from rest_framework import serializers
from main.models import MyUser


class UserSerializer(serializers.Serializer):
    email = serializers.CharField()
    nickname = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    avatar = serializers.ImageField()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 
                  'nickname', 
                  'name', 
                  'description',
                  'avatar'
                ]



class FollowersSerializer(serializers.Serializer):
    follower = UserCreateSerializer(many=True)
    following = UserCreateSerializer(many=True)


class FollowersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['follower', 
                  'following'
                ]



class PublicationsSerializer(serializers.Serializer):
    p_type = serializers.CharField()
    author = UserCreateSerializer(many=True)
    file = serializers.FileField()


class PublicationsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['p_type', 
                  'author',
                  'file'
                ]
        


class LikesSerializer(serializers.Serializer):
    author = UserCreateSerializer(many=True)
    publication = PublicationsCreateSerializer(many=True)


class LikesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['author', 
                  'publication'
                ]



class CommentSerializer(serializers.Serializer):
    author = UserCreateSerializer(many=True)
    publication = PublicationsCreateSerializer(many=True)
    text = serializers.CharField()


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['author', 
                  'publication',
                  'text'
                ]



class ViewSerializer(serializers.Serializer):
    author = UserCreateSerializer(many=True)
    publication = PublicationsCreateSerializer(many=True)


class ViewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['author', 
                  'publication'
                ]
