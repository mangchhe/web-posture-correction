from django.urls import path, include
from Videos import views

urlpatterns = [
    path('search', views.search, name='search'),
    path('level', views.level, name='level'),
    path('', views.main, name='main'),
    path('VideoShow/video_id=<int:video_id>', views.VideoShow, name='VideoShow'),
]
