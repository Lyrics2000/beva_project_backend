from django.urls import path,include
from .views import restricted


urlpatterns = [
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
    path('restricted/',restricted)


]