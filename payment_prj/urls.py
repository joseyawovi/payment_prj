from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("", include("core.urls")),
    path("user/", include("userauths.urls")),
    path('admin/', admin.site.urls),
]
