
from django.urls import path
from app import views
urlpatterns = [
    path('', views.postList, name='postList'),
    path('draftList/', views.draftList, name='draftList'),
    path('postDetail/<int:pk>/', views.postDetail, name='postDetail'),
    path('draftDetail/<int:pk>/', views.draftDetail, name='draftDetail'),
    path('postDelete/<int:pk>/', views.postDelete, name='postDelete'),
    path('draftDelete/<int:pk>/', views.draftDelete, name='draftDelete'),
    path('postCreate/', views.postCreate, name='postCreate'),
    path('postUpdate/<int:pk>/', views.postUpdate, name='postUpdate'),
    path('draftPublish/<int:pk>/', views.draftPublish, name='draftPublish')

]
