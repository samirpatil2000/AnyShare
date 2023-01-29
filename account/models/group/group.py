from django.db import models


class Group(models.Model):

    name = models.CharField(max_length=30)
    admin = models.ManyToManyField("account.Account", blank=True)

    def __str__(self):
        return self.name