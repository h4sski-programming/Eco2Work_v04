from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile_view, name='profile_view'),
    path('show/<int:year>-<int:month>/', views.show_view, name='show_view'),
    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
]