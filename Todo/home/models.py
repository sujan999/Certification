from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

STATUS = [
    ('pen', 'pending'),
    ('com', 'completed')
]


class Todo(models.Model):
    title = models.CharField(max_length=100, unique=True)
    status = models.CharField(choices=STATUS, default='pen', max_length=20)

    date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home:pending", kwargs={"name": self.title})

    def get_absolute_url(self):
        return reverse("home:completed", kwargs={"name": self.title})
