from django.db import models


# Create your models here.
class fileupload(models.Model):
    CHOICES = (
        ('GCL', 'Google Cloud Storage'),
        ('AWS', 'Amazon Web Services Storage')
    )
    file = models.URLField()
    fileType = models.CharField(max_length=128)
    location = models.CharField(choices=CHOICES, default='GCL', max_length=128)
    hash = models.CharField(max_length=128, default='NONE')
    status = models.CharField(max_length=128,default="OK")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
