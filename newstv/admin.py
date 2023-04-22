from django.contrib import admin
from newstv.models import Channel

# Register your models here.

class ChannelAdmin(admin.ModelAdmin):
    list_display=('channel_id','channel_name','channel_image','channel_url','created_date')

admin.site.register(Channel,ChannelAdmin)