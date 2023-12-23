from django.db import models
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class MyUserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        email: str,
        nickname: str,
        name: str,
        description: str,
        avatar: str,
        password: str
    ) -> 'MyUser':

        if not email:
            raise ValidationError('email required')
        if not nickname:
            raise ValidationError('nickname required')

        custom_user: 'MyUser' = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            name=name,
            description=description,
            avatar=avatar,
            password=password
        )
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'MyUser':

        custom_user: 'MyUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.is_superuser = True
        custom_user.is_active = True
        custom_user.is_staff = True
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return


class MyUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name='почта/логин',
        unique=True,
        max_length=200
    )
    nickname = models.CharField(
        verbose_name='ник',
        max_length=20
    )
    name = models.CharField(
        verbose_name='настоящее имя пользователя',
        max_length=20,
        null=True
    )
    description = models.CharField(
        verbose_name='описание',
        max_length=200,
        null=True
    )
    avatar = models.ImageField(
        verbose_name="изображение",
        upload_to='images/',
        null=True
    )
    is_staff = models.BooleanField(
        verbose_name='staff',
        default=False
    )
    
    objects = MyUserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Followers(models.Model):

    follower = models.ForeignKey(
        verbose_name='подпищик',
        related_name='followings',
        to=MyUser,
        on_delete=models.CASCADE
    )

    following = models.ForeignKey(
        verbose_name='кому подщикнулись',
        related_name='folllowers',
        to=MyUser,
        on_delete=models.CASCADE
    )


class Publications(models.Model):
    class Types(models.TextChoices):
        REEL = 'reel'
        IMAGE = 'image'

    p_type = models.CharField(
        verbose_name='валюта',
        max_length=6,
        choices=Types.choices,
        default=Types.IMAGE
    )
    author = models.ForeignKey(
        verbose_name='автор поста',
        related_name='posts',
        to=MyUser,
        on_delete=models.CASCADE
    )
    file = models.FileField(
        verbose_name="пост",
        upload_to='img/'
    )


class History(models.Model):
    author = models.ForeignKey(
        verbose_name='автор истории',
        related_name='histories',
        to=MyUser,
        on_delete=models.CASCADE
    )
    file = models.FileField(
        verbose_name="история",
        upload_to='img/'
    )
    created_at = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(default=(timezone.now() + datetime.timedelta(days=1)))


class Likes(models.Model):
    author = models.ForeignKey(
        verbose_name='автор лайка',
        related_name='likes',
        to=MyUser,
        on_delete=models.CASCADE
    )
    publication = models.ForeignKey(
        verbose_name='пост',
        related_name='lpost',
        to=Publications,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ['author', 'publication']

class Comments(models.Model):
    author = models.ForeignKey(
        verbose_name='автор комента',
        related_name='comments',
        to=MyUser,
        on_delete=models.CASCADE
    )
    publication = models.ForeignKey(
        verbose_name='пост',
        related_name='cpost',
        to=Publications,
        on_delete=models.CASCADE
    )
    text = models.CharField(
        verbose_name='камент',
        max_length=150
    )

class View(models.Model):
    author = models.ForeignKey(
        verbose_name='автор просмотра',
        related_name='views',
        to=MyUser,
        on_delete=models.CASCADE
    )
    publication = models.ForeignKey(
        verbose_name='пост',
        related_name='vpost',
        to=Publications,
        on_delete=models.CASCADE
    )