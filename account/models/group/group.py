from django.db import models


class Group(models.Model):

    name = models.CharField(max_length=30)
    admin = models.ManyToManyField("account.Account", blank=True)

    created_at = models.DateTimeField(verbose_name='date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='date of update', auto_now=True)

    def __str__(self):
        return self.name