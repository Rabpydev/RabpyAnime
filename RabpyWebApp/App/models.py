from django.db import models
from django.utils.html import format_html

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Anime(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desctipion = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    role = models.CharField(max_length=100)
    weapon = models.CharField(max_length=100)
    ability = models.CharField(max_length=100)
    anime = models.ManyToManyField(Anime, blank=True)
    image = models.ImageField(upload_to='App/files/character_image', null=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + ", " + str(self.create_date)
    
    def show_image(self):
        if self.image:
            return format_html('<img src="' + self.image.url + '" height="50px">')
        return ''
    show_image.allow_tags = True