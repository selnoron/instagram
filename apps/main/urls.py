from django.urls import path
from main.viewes.normal_vi import AuthView, RegisView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('auth/', AuthView.as_view()),
    path('', RegisView.as_view()),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
