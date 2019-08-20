from django.db import models

class Tweets(models.Model):
    name = models.CharField(max_length=30)
    contents = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tweets"
