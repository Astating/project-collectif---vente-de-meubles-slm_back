from django.db import models

class Furnitures (models.Model):
    TYPE_CHOICES = [
        ('Bed'),
        ('Chair'),
        ('Table'),
        ('Couch'),
        ('Closet'),
    ]
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
    )

    price = models.FloatField
    COLOR_CHOICES = [
        ('Black'),
        ('White'),
        ('Grey'),
        ('Brown'),
        ('Yellow'),
        ('Blue'),
        ('Green'),
        ('Red'),
        ('Pink'),
        ('Purple'),
    ]
    color = models.CharField(
        max_length=10,
        choices=COLOR_CHOICES,
    )
    CONDITION_CHOICES = [
        ('New'),
        ('Good'),
        ('Used'),
        ('Old'),
    ]
    condition = models.CharField(
        max_length=10,
        choices=CONDITION_CHOICES,
    )
    MATERIAL_CHOICES = [
        ('Wood'),
        ('Metal'),
        ('Plastic'),
        ('Leather'),
        ('Wool'),

    ]
    material = models.CharField(
        max_length=10,
        choices=MATERIAL_CHOICES,
    )
    dimension = models.CharField
    stock = models.BooleanField

class Outil (models.Model):
    title = models.CharField(max_length=100)
    objects = Furnitures()
    
outil = Outil.objects("Notre fourniture")
    

