from django.urls import path
from . import views
urlpatterns=[
    path("login/",views.login),
    path("signup/",views.signup),
    path("getPosts/",views.getPosts),
    path("makePost/",views.makePost),
    path("bestPosts/",views.bestPosts), # To be done
    path("acceptPost/",views.acceptPost),# To be done
    path("postDetails/",views.postDetails),
]