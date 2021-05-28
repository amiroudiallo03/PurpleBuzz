from django.db import models

# Create your models here.
class Convention(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        abstract = True


class BannerWork(Convention):
    titre = models.CharField(max_length=200)
    sous_titre = models.CharField(max_length=200)
    description = models.TextField()
    Image = models.FileField(upload_to="banner_work_image")

    class Meta:
        verbose_name = ("BannerWork")
        verbose_name_plural = ("BannerWorks")

    def __str__(self):
        return self.titre

class FuturedWork(Convention):
    nom = models.CharField(max_length=200)
    titre = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = ("FuturedWork")
        verbose_name_plural = ("FuturedWork")

    def __str__(self):
        return self.titre

class Image(Convention):
    titre = models.CharField(max_length=200)
    image = models.FileField(upload_to="image_futuredwork")

    class Meta:
        verbose_name = ("Image")
        verbose_name_plural = ("Images")

    def __str__(self):
        return self.titre 

class Pricing(Convention):
    titre = models.CharField(max_length=200)
    sous_titre =  models.CharField(max_length=200)
    image =  models.FileField(upload_to="image_pricing")

    class Meta:
        verbose_name = ("Pricing")
        verbose_name_plural = ("Pricing")

    def __str__(self):
        return self.titre

class Pack(Convention):
    icone = models.CharField(max_length=200)
    titre = models.CharField(max_length=200)
    sous_titre =  models.CharField(max_length=200)
    prix = models.IntegerField()
    periode = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("Pack")
        verbose_name_plural = ("Packs")

    def __str__(self):
        return self.titre

class Avantage(Convention):
    nom = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("Avantage")
        verbose_name_plural = ("Avantages")

    def __str__(self):
        return self.nom

class Categorie(Convention):
    nom = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("Categorie")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.nom

class Card(Convention):
    image = models.FileField(upload_to="image_card")
    titre = models.CharField(max_length=200)
    sous_titre = models.CharField(max_length=200)
    categorie = models.ForeignKey("Categorie",on_delete=models.CASCADE, related_name="image_card")

    class Meta:
        verbose_name = ("Card")
        verbose_name_plural = ("Cards")

    def __str__(self):
        return self.titre


class CategorieWork(Convention):
    nom = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("CategorieWork")
        verbose_name_plural = ("CategorieWorks")

    def __str__(self):
        return self.nom

class Work(Convention):
    titre = models.CharField(max_length=200)
    sous_titre =  models.CharField(max_length=200)
    image = models.FileField(upload_to="image_work")
    categorie = models.ForeignKey("CategorieWork", related_name="work_categorie", on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Work")
        verbose_name_plural = ("Works")

    def __str__(self):
        return self.titre 
