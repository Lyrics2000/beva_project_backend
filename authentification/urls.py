from django.urls import path,include
from .views import login_app,signup_view,activate_account,logout_user

app_name = "authentification"
urlpatterns = [
    path('',login_app,name="login"),
    path('logout',logout_user,name="logout"),
    path('signup/',signup_view,name="sign_up"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate_account, name='activate')
]