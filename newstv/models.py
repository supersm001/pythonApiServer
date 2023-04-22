from django.db import models

# Create your models here.

# Creating NewsTv Channel Model

class Channel(models.Model):
    channel_id= models.AutoField(primary_key=True)
    channel_name= models.CharField(max_length=255)
    channel_image= models.CharField(max_length=255)
    # channel_image= models.ImageField(upload_to='static')
    channel_url= models.CharField(max_length=255)
    created_date= models.DateTimeField(auto_now=True)