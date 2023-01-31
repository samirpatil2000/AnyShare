from rest_framework import serializers
from post.models import Post, Comment



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.email', read_only=True)
    post_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ["content", "author", "post_id"]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data["author_id"] = user.id if user.is_authenticated else 1
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.author_id != user.id:
            raise "Not Authorized"
        return super().update(instance, validated_data)


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.CharField(source='author.email', read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "comments", "author", "created_at"]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data["author_id"] = user.id if user.is_authenticated else 1
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.author_id != user.id:
            raise "Not Authorized"
        return super().update(instance, validated_data)

