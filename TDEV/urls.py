from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm



urlpatterns=[
    path("",views.index,name='index'),
    path("TDEV/login/home",views.home,name='home'),
    path('TDEV/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('register/',views.RegistrationView.as_view(),name='register'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)