from django.contrib import admin
from messaging.models import Message
from messaging.models import UserProfile
admin.site.register(UserProfile)
admin.site.register(Message)

