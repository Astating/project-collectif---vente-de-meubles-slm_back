from django.db import models


class Furnitures (models.Model):
    class Type(models.TextChoices):
        BED = 'Bed', ('Bed')
        CHAIR = 'Chair', ('Chair')
        TABLE = 'Table', ('Table')
        COUCH = 'Couch', ('Couch')
        CLOSET = 'Closet', ('Closet')

    type = models.CharField(
        max_length=10,
        choices=Type.choices,
        default=Type.BED
    )

    class Color(models.TextChoices):
        BLACK = 'Black', ('Black')
        WHITE = 'White', ('White')
        GREY = 'Grey', ('Grey')
        BROWN = 'Brown', ('Brown')
        YELLOW = 'Yellow', ('Yellow')

    color = models.CharField(
        max_length=10,
        choices=Color.choices,
        default=Color.GREY
    )

    class Condition(models.TextChoices):
        NEW = 'New', ('New')
        GOOD = 'Good', ('Good')
        USED = 'Used', ('Used')
        OLD = 'Old', ('Old')
    condition = models.CharField(
        max_length=10,
        choices=Condition.choices,
        default=Condition.USED
    )

    class Material(models.TextChoices):
        WOOD = 'Wood', ('Wood')
        METAL = 'Metal', ('Metal')
        PLASTIC = 'Plastic', ('Plastic')
        LEATHER = 'Leather', ('Leather')
        WOOL = 'Wool', ('Wool')
    material = models.CharField(
        max_length=10,
        choices=Material.choices,
        default=Material.WOOD
    )


price = models.FloatField
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
