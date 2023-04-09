from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('home', views.index, name='index'),
    path('newnote', views.newnote, name='newnote'),
    path('<note_id>', views.delete_note, name='delete_note'),
]