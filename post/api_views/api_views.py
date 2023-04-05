import json

from post.models import Post, Comment
from post.api_views.generic_views import CustomAPIView
from post.models.post import LatLong
from post.serializers import PostSerializer, CommentSerializer, LatLongSerializer


class CommentAPIView(CustomAPIView):
    serializer_class = CommentSerializer

    def dispatch(self, request, *args, **kwargs):
        self.post_id = kwargs.get('post_id', "any_default")
        return super(CommentAPIView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.post_id)


class PostAPIView(CustomAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status






@api_view(['GET', 'POST'])
def lat_logs(request):
    if not request.user.is_authenticated:
        response = {"message": "User not authenticated"}
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'GET':
        latlong = LatLong.objects.filter(user_id=request.user.id)
        serializer = LatLongSerializer(latlong, many=True)
        response = {"message": "Data Loaded Successfully", "data": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = LatLongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            response = {"message": "Data Added Successfully"}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {"message": "Invalid data"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

