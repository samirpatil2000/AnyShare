from rest_framework import serializers
from post.models import Post, Comment, LatLong


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.email', read_only=True)

    class Meta:
        model = Comment
        fields = ["content", "author"]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data["author_id"] = user.id if user.is_authenticated else 1
        validated_data["post_id"] = self.context.get('request').parser_context.get('kwargs').get(
            'post_id')
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.author_id != user.id:
            raise "Not Authorized"
        return super().update(instance, validated_data)


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.CharField(source='author.email', read_only=True)
    group_id = serializers.IntegerField(source="group.id", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "created_at", "group_id", "comments"]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data["author_id"] = user.id if user.is_authenticated else 1
        validated_data["group_id"] = 1
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.author_id != user.id:
            raise "Not Authorized"
        return super().update(instance, validated_data)



class LatLongSerializer(serializers.ModelSerializer):

    class Meta:
        model = LatLong
        fields = ["latitude", "longitude", "created_at"]
