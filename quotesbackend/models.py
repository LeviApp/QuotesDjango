from django.db import models

# Create your models here.

class Quotes(models.Model):
    title = models.CharField(max_length=50)
    text_body = models.TextField()
    img_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
