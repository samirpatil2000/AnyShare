from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey("account.Account", on_delete=models.CASCADE)
    group = models.ForeignKey("account.Group", on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name='date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='date of update', auto_now=True)

    def __str__(self):
        return self.title
