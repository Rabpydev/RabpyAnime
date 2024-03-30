from django.db import models
from django.utils.html import format_html

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Anime(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, null=True, blank=True, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    year = models.IntegerField()
    score = models.FloatField()
    source = models.CharField(max_length=50)
    image = models.ImageField(upload_to='App/files/anime_image', null=True)
    country = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
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
    type = models.CharField(max_length=10)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + ", " + str(self.create_date)
    
    def show_image(self):
        if self.image:
            return format_html('<img src="' + self.image.url + '" height="50px">')
        return ''
    show_image.allow_tags = True


class ResourceAnime(models.Model):
    anime = models.ForeignKey(Anime, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



class ResourceCharacter(models.Model):
    character = models.ForeignKey(Character, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)