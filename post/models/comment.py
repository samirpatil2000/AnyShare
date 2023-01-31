from django.db import models


class Comment(models.Model):

    author = models.ForeignKey("account.Account", on_delete=models.CASCADE)
    post = models.ForeignKey("post.post", on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name='date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='date of update', auto_now=True)

    def __str__(self):
        return self.author + " " + self.post
