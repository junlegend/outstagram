from django.db import models

class User(models.Model):
    name     = models.CharField(max_length=50)
    email    = models.EmailField()
    password = models.CharField(max_length=200)
    mobile   = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'

