from django.db import models
import datetime


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_joined = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateField(default=datetime.date.today)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    posted_at = models.DateField(default=datetime.date.today)
    description = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.name
