from django.db import models
from django.contrib.auth.models import User

#abstract super class for user profiles and groups
class Recipient(models.Model):
    is_group_recipient = models.BooleanField(default=False)

#Group definition
class Group(Recipient):
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=1024)
    owner = models.ForeignKey(User, related_name="owned_groups")
    members = models.ManyToManyField(User, related_name='messaging_groups')

#owner = 1 to many, members = many to many

#specify default order
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

#Message definition
class Message(models.Model):
    text = models.CharField(max_length=512, unique=False)
    time = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, related_name='sent_messages')
    recipient = models.ForeignKey(Recipient, related_name='messages')

    def __unicode__(self):
        return "From: %s to %s: %s" % (self.sender, self.recipient, self.text)

#User profile definition, first one mapping to user, contacts is many to many between users and user profiles
class UserProfile(Recipient):
    user = models.OneToOneField(User, related_name='profile')
    introduction = models.CharField(max_length=1024)
    contacts = models.ManyToManyField(User)

    def __unicode__(self):
        return self.user.username

    class Meta:
        ordering = ['user__last_name', 'user__first_name']
