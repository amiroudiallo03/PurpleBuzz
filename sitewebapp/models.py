from django.db import models

# Create your models here.
class Convention(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class BannerHome(Convention):
    titre = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = ("Bannerhome")
        verbose_name_plural = ("Bannerhomes")

    def __str__(self):
        return self.titre


class Website(Convention):
    titre_site = models.CharField(max_length=200)
    description_site = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    copyright = models.CharField(max_length=200)
    titre_contact = models.CharField(max_length=200)
    sous_titre_contact =  models.CharField(max_length=200)
    description_contact =  models.TextField()
    titre_team = models.CharField(max_length=200)
    description_team = models.TextField()

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

    def __str__(self):
        return self.titre_site
    
class About(Convention):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField()

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.titre

class Team(Convention):
    image = models.FileField(upload_to="image_team")
    nom = models.CharField(max_length=200)
    job = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.nom


class Partner(Convention):
    icone = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return self.icone


class Creative(Convention):
    titre = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'Creative'
        verbose_name_plural = 'Creatives'

    def __str__(self):
        return self.titre

    
class Progress(Convention):
    titre = models.CharField(max_length=200)
    progres = models.IntegerField()

    class Meta:
        verbose_name = 'Progress'
        verbose_name_plural = 'Progress'

    def __str__(self):
        return self.titre

class CardAbout(Convention):
    icone = models.CharField(max_length=200)
    titre = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'CardAbout'
        verbose_name_plural = 'CardAbouts'

    def __str__(self):
        return self.titre

class Newsletter(Convention):
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletter'

    def __str__(self):
        return self.email

class BannerContact(Convention):
    titre = models.CharField(max_length=200)
    sous_titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to="image_contact")

    class Meta:
        verbose_name = 'BannerContact'
        verbose_name_plural = 'BannerContacts'

    def __str__(self):
        return self.titre

class Contact(Convention):
    job = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
   
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        
    def __str__(self):
        return self.titre

class Service(Convention):
    titre = models.CharField(max_length=200)
    sous_titre = models.CharField(max_length=200)
    description = models.TextField()
   
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        
    def __str__(self):
        return self.titre

class AboutChoice(Convention):
    image = models.FileField(upload_to="image_choice")
    titre = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'AboutChoice'
        verbose_name_plural = 'AboutChoice'
        
    def __str__(self):
        return self.titre

class Icone(Convention):
    nom = models.CharField(max_length=200)
    icone = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Icone'
        verbose_name_plural = 'Icones'
        
    def __str__(self):
        return self.nom

class ReseauSociaux(Convention):
    nom =  models.CharField(max_length=200)
    icone = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'ReseauSocial'
        verbose_name_plural = 'ReseauSociaux'
        
    def __str__(self):
        return self.nom
