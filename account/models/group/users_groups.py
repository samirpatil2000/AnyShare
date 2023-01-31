from django.db import models


class UsersGroups(models.Model):

    user = models.ForeignKey("account.Account", on_delete=models.CASCADE)
    group = models.ForeignKey("account.Group", on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name='date of creation', auto_now_add=True)

    def __str__(self):
        return str(self.user) + " - " + self.group.name
