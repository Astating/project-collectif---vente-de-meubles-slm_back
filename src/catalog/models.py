from django.db import models


class Furnitures (models.Model):  # Classe mère
    #id qui s'incrémente
    id = models.AutoField(primary_key=True)
    #champ qui permet a l'utilisateur de remplir en prix
    price = models.FloatField(default=0.0)
    #Champ qui permet a l'utilisateur de remplir une dimension
    dimension = models.CharField(max_length=255, default='100x200x200')
    #Case a coché en stock ou non 
    stock = models.BooleanField(default=True)
    #Block de description des items
    description = models.TextField(default='Add a description of your item here.')
    #Block de titre
    title = models.CharField(max_length=255,default='Add a title here.')
    img = models.ImageField(upload_to= 'images', default='upload images')

    class Type(models.TextChoices):  # Sous classe
        # Tableau de valeur
        BED = 'Bed', ('Bed')
        CHAIR = 'Chair', ('Chair')
        TABLE = 'Table', ('Table')
        COUCH = 'Couch', ('Couch')
        CLOSET = 'Closet', ('Closet')

    # On dit que le type comprend un champ en string qui ne peut pas dépasser 10 caractères,
    # On dit que le type de fourniture sera sous forme de choix
    # On définit aussi le type de fourniture par défaut (ici Bed)
    type = models.CharField(
        max_length=10,
        choices=Type.choices,
        default=Type.BED
    )

    class Color(models.TextChoices):  # Sous classe
        BLACK = 'Black', ('Black')
        WHITE = 'White', ('White')
        GREY = 'Grey', ('Grey')
        BROWN = 'Brown', ('Brown')
        YELLOW = 'Yellow', ('Yellow')
        BLUE = 'Blue', ('Blue')
        RED = 'Red', ('Red')
        PINK = 'Pink', ('Pink')
        GREEN = 'Green', ('Green')



    # On dit que la couleur comprend un champ en string qui ne peut pas dépasser 10 caractères,
    # On dit que la couleur de fourniture sera sous forme de choix
    # On définit aussi la couleur de fourniture par défaut (ici Bed)
    color = models.CharField(
        max_length=10,
        choices=Color.choices,
        default=Color.GREY
    )

    class Condition(models.TextChoices):  # Sous classe
        NEW = 'New', ('New')
        LIKENEW = 'Like New', ('Like New')
        GOOD = 'Good', ('Good')
        USED = 'Used', ('Used')
        OLD = 'Old', ('Old')

    # On dit que le type comprend un champ en string qui ne peut pas dépasser 10 caractères,
    # On dit que le type de fourniture sera sous forme de choix
    # On définit aussi le type de fourniture par défaut (ici Bed)
    condition = models.CharField(
        max_length=10,
        choices=Condition.choices,
        default=Condition.USED
    )

    class Material(models.TextChoices):  # Sous classe
        WOOD = 'Wood', ('Wood')
        METAL = 'Metal', ('Metal')
        PLASTIC = 'Plastic', ('Plastic')
        LEATHER = 'Leather', ('Leather')
        WOOL = 'Wool', ('Wool')
        MARBLE = 'Marble', ('Marble')
        CLOTH = 'Cloth', ('Cloth')
        SUEDE = 'Suede', ('Suede')
        


    # On dit que le matériel comprend un champ en string qui ne peut pas dépasser 10 caractères,
    # On dit que le matériel de fourniture sera sous forme de choix
    # On définit aussi le matériel de fourniture par défaut (ici Bed)
    material = models.CharField(
        max_length=10,
        choices=Material.choices,
        default=Material.WOOD
    )
