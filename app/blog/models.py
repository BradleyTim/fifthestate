from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Tag(models.Model):
  name = models.CharField(max_length=140)

  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField(max_length=140)
  slug = models.CharField(max_length=140)
  content = RichTextField()
  date_posted = models.DateField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag)

  def __str__(self):
    return self.title
