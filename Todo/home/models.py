from django.db import models

# Create your models here.

# STATUS = (
#('pen', 'pending')
#('com', 'completed')
# )


class Todo(models.Model):
    title = models.CharField(max_length=100, unique=True)
    #status = models.CharField(choice=STATUS, max_length=20)

    date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home:Todo", kwargs={"name": self.title})
