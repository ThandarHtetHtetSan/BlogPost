from django.urls import path
from .import views
from django.contrib.auth.views import LoginView
urlpatterns=[
    path('',views.PostList.as_view(),name='home'),
    path('<slug:slug>/',views.PostDetail.as_view(),name='post_detail'),

]