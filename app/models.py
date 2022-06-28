from django.db import models

# Create your models here.
class Talaba(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=300)
    faculties = models.CharField(max_length=300)
    direction = models.CharField(max_length=300)
    stage = models.IntegerField(max_length=2)
    group = models.IntegerField(max_length=10)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.faculties} fakulteti,\n" \
               f"{self.direction} yo'nalishi, {self.stage}-bosqich, {self.group}-guruh talabasi."