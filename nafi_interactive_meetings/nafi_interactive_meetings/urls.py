from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenBlacklistView

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("screencast.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    # path("api-screencast/", include("screencast.urls")),
    path("api-questions/", include("questions.urls")),
    path("api-token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
]

urlpatterns += [
    path("api-schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api-schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api-schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

# urlpatterns += [re_path(r"^.*", TemplateView.as_view(template_name="index.html"))]
