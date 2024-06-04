from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api-screencast/", include("screencast.urls")),
    path("api-questions/", include("questions.urls")),
    path("api-token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
]

urlpatterns += [re_path(r"^.*", TemplateView.as_view(template_name="index.html"))]
