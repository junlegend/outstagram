from django.db import models
from user.models import User

class Posting(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    image_url  = models.URLField(max_length=2000)
    text       = models.TextField()

    class Meta:
        db_table = 'postings'
