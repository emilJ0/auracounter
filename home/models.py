from django.db import models

class Groups(models.Model):
    group_name = models.CharField(max_length=20)
    group_code = models.CharField(max_length=10)
    group_users = models.JSONField(null=True)
    group_history = models.JSONField(null=True)

    def __str__(self):
        return self.group_name
