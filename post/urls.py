from django.urls import path
from . import api_views


urlpatterns = [
    path('posts/', api_views.PostAPIView.as_view()),
    path('posts/<int:pk>', api_views.PostAPIView.as_view()),
    path('posts/<int:post_id>/comments', api_views.CommentAPIView.as_view())
 ]