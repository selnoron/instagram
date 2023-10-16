from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from main.views import (
    UserViewSet,
    FollowersViewSet,
    PublicationViewSet,
    LikesViewSet,
    CommentViewSet,
    ViewViewSet,
    UserFilterSet,
    PublicationsFilterSet
)

router = DefaultRouter()
router2 = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'followers', FollowersViewSet, basename='follower')
router.register(r'publications', PublicationViewSet, basename='publications')
router.register(r'likes', LikesViewSet, basename='likes')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'view', ViewViewSet, basename='view')
router2.register(r'user_search', UserFilterSet, basename='user_search')
router2.register(r'publications_search', PublicationsFilterSet, basename='pubs_search')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('search/', include(router2.urls))
]


urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]