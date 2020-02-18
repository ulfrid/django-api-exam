from django.db import models


class Users(models.Model):
    name       = models.CharField(max_length=50, null=True)
    email      = models.CharField(max_length=50, null=True, unique=True)
    password   = models.CharField(max_length=400, null=True)
    social_id  = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
