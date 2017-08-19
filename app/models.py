from django.db import models
from tinymce.models import HTMLField


class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)


class Assessment(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)


class Bug(models.Model):
    title = models.CharField(max_length=200)
    body = HTMLField(null=True)
    assessment = models.ForeignKey(Assessment, null=True, on_delete=models.SET_NULL)

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)


class Flag(models.Model):
    title = models.CharField(max_length=100)
    note = HTMLField(null=True)
    done = models.BooleanField(default=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)
