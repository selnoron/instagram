from django.urls import path
from main.viewes.normal_vi import (
    AuthView, 
    RegisView, 
    MainView, 
    LikeView,
    ComView,
    HisView,
    DisView
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('auth/', AuthView.as_view()),
    path('', RegisView.as_view()),
    path('inst/', MainView.as_view()),
    path('inst/post/<int:pk>/like/', LikeView.as_view()),
    path('inst/post/<int:pk>/comm/', ComView.as_view()),
    path('inst/his/<int:pk>/', HisView.as_view()),
    path('inst/us/<int:pk>/', HisView.as_view()),
    path('dis/', DisView.as_view())
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
