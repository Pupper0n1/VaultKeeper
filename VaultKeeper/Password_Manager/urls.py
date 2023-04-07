from django.urls import path, reverse, reverse_lazy, include
from . import views

app_name = 'Password_Manager'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('passwords/', views.password_view, name='passwords'),
    path('passwords/delete/<int:pk>', views.delete_view, name='delete'),
    path('about/', views.about_view, name='about'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/passwords/', views.password_view),
    path('accounts/logout/thankyou/', views.thankyou_view, name='thankyou')
]
