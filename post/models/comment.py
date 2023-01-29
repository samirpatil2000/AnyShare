from django.db import models


class Comment(models.Model):

    author = models.ForeignKey("account.Account", on_delete=models.CASCADE)
    post = models.ForeignKey("post.post", on_delete=models.CASCADE)


    def __str__(self):
        return self.author + " " + self.post
