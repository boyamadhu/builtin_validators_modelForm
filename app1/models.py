from django.db import models

# Create your models here.

class Topic(models.Model):
    topic=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic