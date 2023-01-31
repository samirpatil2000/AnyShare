from post.models import Post, Comment
from post.api_views.generic_views import CustomAPIView
from post.serializers import PostSerializer, CommentSerializer




class CommentAPIView(CustomAPIView):
    Model = Comment
    queryset = Model.objects.all()
    serializer_class = CommentSerializer


class PostAPIView(CustomAPIView):
    Model = Post
    queryset = Model.objects.all()
    serializer_class = PostSerializer



# @csrf_exempt
# def like_post(request, post_id: int):
#     if request.method == "POST":
#         try:
#             Like.objects.get_or_create(post_id=post_id, user_id=request.user.id or 1)
#             result = {"status": status.HTTP_200_OK, "message": "Post Successfully Liked..!", "data": {}}
#         except Exception as e:
#             result = {"status": status.HTTP_400_BAD_REQUEST, "message": str(e), "data": {}}
#         return JsonResponse(result)


