from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import (
    UserViewSet,
    FollowersViewSet,
    PublicationViewSet,
    LikesViewSet,
    CommentViewSet,
    ViewViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'followers', FollowersViewSet, basename='follower')
router.register(r'publications', PublicationViewSet, basename='publications')
router.register(r'likes', LikesViewSet, basename='likes')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'View', ViewViewSet, basename='view')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]


urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)