from django.db import models

class Search(model.Model):
    text = models.TextField()
