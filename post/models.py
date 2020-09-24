from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)
TRENDING = (
    (0, 'False'),
    (1, 'True')
)

SlIDE = (
    (0, 'False'),
    (1, 'True')
)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/%y/%m/%d/', blank=False)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    trending = models.IntegerField(choices=TRENDING, default=0)
    slideshow = models.IntegerField(choices=SlIDE, default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Topbar(models.Model):
    topic = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

