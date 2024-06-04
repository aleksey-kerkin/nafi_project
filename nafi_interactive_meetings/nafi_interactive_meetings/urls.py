from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api-screencast/", include("screencast.urls")),
    path("api-questions/", include("questions.urls")),
]

urlpatterns += [re_path(r"^.*", TemplateView.as_view(template_name="index.html"))]
