from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    icon = models.URLField()

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.code


class Theme(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )

    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    photo = models.URLField()

    def __str__(self):
        return self.name


class Word(models.Model):
    name = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    transcription = models.CharField(max_length=255)
    example = models.TextField()
    sound = models.URLField()
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
