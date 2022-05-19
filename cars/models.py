from django.db import models

class Samochod (models.Model):
    rocznik=models.IntegerField(default=None)
    marka=models.CharField(max_length=50)
    model=models.CharField(max_length=20)
    kolor=models.CharField(max_length=15)
    generacja=models.IntegerField(default=None)

    def __str__(self):
        return f'{self.marka}'

    class Meta:
        verbose_name="Brand"

class Kierowca(models.Model):
    imie=models.CharField(max_length=20)
    nazwisko=models.CharField(max_length=20)
    doswiadczenie=models.IntegerField(default=None)


    def __str__(self):
        return f'{self.imie}'

    class Meta:
        verbose_name="Name"

class Ubezpieczenie(models.Model):
    ubezpieczenie=models.CharField(max_length=20)
    koszt_ubezpieczenia=models.IntegerField(default=None)

    def __str__(self):
        return f'{self.ubezpieczenie}'

    class Meta:
        verbose_name="Insurance"