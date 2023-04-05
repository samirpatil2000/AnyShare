from django.db import models

from post.models import Comment


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey("account.Account", on_delete=models.CASCADE)
    group = models.ForeignKey("account.Group", on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name='date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='date of update', auto_now=True)

    def __str__(self):
        return self.title

    @property
    def comments(self):
        return Comment.objects.filter(post_id=self.id)


class LatLong(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    user = models.ForeignKey("account.Account", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='date of creation', auto_now_add=True)

    def __str__(self):
        return self.latitude + " - " + self.longitude