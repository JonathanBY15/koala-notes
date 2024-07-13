from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('api/notes', views.note_list_create, name='note-list-create'),
    path('api/notes/<int:pk>', views.note_detail, name='note-detail'),
]
