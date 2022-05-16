from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('color-lab.poll/', include('app.urls')),
    path('admin/', admin.site.urls),
]
