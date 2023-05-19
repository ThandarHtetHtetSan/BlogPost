from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('blog_view',views.blog_view,name='blog_view'),
    path('<int:id>/',views.detail_view,name='detail_view')
]