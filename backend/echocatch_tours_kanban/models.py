from uuid import uuid4
from base64 import urlsafe_b64encode
from django.db import models

def short_uuid():
    return urlsafe_b64encode(uuid4().bytes).decode('utf8').rstrip('=')

class Swimlane(models.Model):
    id = models.CharField(primary_key=True, max_length=22, default=short_uuid)
    name = models.CharField(max_length=255)
    position = models.PositiveSmallIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'swimlane'
        ordering = ['position']
        indexes = [
            models.Index(fields=['position']),
        ]

class Boat(models.Model):
    id = models.CharField(primary_key=True, max_length=22, default=short_uuid)
    name = models.CharField(max_length=255)

    swimlane = models.ForeignKey(Swimlane, on_delete=models.CASCADE, related_name='boats')
    position = models.PositiveSmallIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'boat'
        ordering = ['swimlane__position', 'position']
        indexes = [
            models.Index(fields=['position']),
        ]
