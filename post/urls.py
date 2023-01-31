from django.urls import path
from . import api_views


urlpatterns = [
    path('posts/', api_views.PostAPIView.as_view()),
 ]