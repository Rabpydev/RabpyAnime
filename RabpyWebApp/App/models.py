from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    role = models.CharField(max_length=100)
    weapon = models.CharField(max_length=100)
    ability = models.CharField(max_length=100)
    image = models.ImageField(upload_to='App/files/character_image')
    create_date = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.name + ", " + str(self.create_date)