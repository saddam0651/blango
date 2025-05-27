from django.db import models
from django.conf import settings


# Create your models here.
class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content_object = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", db_index=True)
    content = models.TextField(max_length=100)

    def __str__(self):
        return self.content


class AuthorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField()

    def __str__(self):
        return f"{self.__class__.__name__} object for {self.user}"