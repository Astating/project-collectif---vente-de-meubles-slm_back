from django.db import models

class Furnitures (models.Model):
    class Type(models.TextChoices):
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
    class Colors(models.TextChoices):
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
    class Conditions(models.TextChoices):
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
    class Materials(models.TextChoices):
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

"""class Outil (models.Model):
    title = models.CharField(max_length=100)
    objects = Furnitures()
    
outil = Outil.objects("Notre fourniture")
    

class Student(models.Model):

    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')
        GRADUATE = 'GR', _('Graduate')

    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )"""