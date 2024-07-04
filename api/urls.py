from django.urls import path
from . import views
urlpatterns=[
    path("login/",views.login),
    path("signup/",views.signup),
    path("getPosts/",views.getPosts),
    path("makePost/",views.makePost),
    path("bestPosts/",views.bestPosts),
    path("acceptPost/",views.acceptPost)
]