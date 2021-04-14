from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.URLField()


class Level(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=2)


class Theme(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    photo = models.URLField()


class Word(models.Model):
    name = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    transcription = models.CharField(max_length=255)
    example = models.CharField()
    sound = models.URLField()
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL)
