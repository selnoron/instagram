from rest_framework import serializers
from main.models import MyUser, Followers, Publications, Likes, Comments, View


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
    follower = UserSerializer(many=False, read_only=True)
    following = UserSerializer(many=False, read_only=True)


class FollowersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields = ['follower', 
                  'following'
                ]



class PublicationsSerializer(serializers.Serializer):
    p_type = serializers.CharField()
    author = UserSerializer(many=False, read_only=True)
    file = serializers.FileField()


class PublicationsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = ['p_type', 
                  'author',
                  'file'
                ]
        


class LikesSerializer(serializers.Serializer):
    author = UserSerializer(many=False, read_only=True)
    publication = PublicationsSerializer(many=False, read_only=True)


class LikesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['author', 
                  'publication'
                ]



class CommentSerializer(serializers.Serializer):
    author = UserSerializer(many=False, read_only=True)
    publication = PublicationsSerializer(many=False, read_only=True)
    text = serializers.CharField()


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['author', 
                  'publication',
                  'text'
                ]



class ViewSerializer(serializers.Serializer):
    author = UserSerializer(many=False, read_only=True)
    publication = PublicationsSerializer(many=False, read_only=True)


class ViewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ['author', 
                  'publication'
                ]
