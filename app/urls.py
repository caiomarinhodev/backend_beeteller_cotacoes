from django.urls import path, include
from knox import views as knox_views

from app.viewsets import SignUpAPI, SignInAPI, MainUser

urlpatterns = []

urlpatterns += [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('kraken/', include('krakenapi.urls')),
    path('awesome/', include('awesomeapi.urls')),
    path('auth/register/', SignUpAPI.as_view()),
    path('auth/login/', SignInAPI.as_view()),
    path('auth/user/', MainUser.as_view()),
    path('auth/logout/', knox_views.LogoutView.as_view(), name="knox-logout"),
]
