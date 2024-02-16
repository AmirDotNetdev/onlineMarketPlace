from django.db import models

from django.contrib.auth.models import User
from item.models import Item

class Conversation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)
        def __str__(self):
            return self.item
        

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        def __str__(self):
            return self.content
        
