from post.models import Post, Comment
from post.api_views.generic_views import CustomAPIView
from post.serializers import PostSerializer, CommentSerializer


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
