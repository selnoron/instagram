from rest_framework import serializers
from main.models import MyUser, Followers, Publications, History, Likes, Comments, View


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
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
    pk = serializers.IntegerField()
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
        

class HistorySerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    author = UserSerializer(many=False, read_only=True)
    file = serializers.FileField()
    created_at = serializers.DateTimeField()
    expiration_date = serializers.DateTimeField()


class HistoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['author',
                  'file',
                  'created_at',
                  'expiration_date'
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
