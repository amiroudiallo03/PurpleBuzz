from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
# Register your models here.

@admin.register(models.BannerHome)
class BannerHomeAdmin(admin.ModelAdmin):
    list_display = ('titre','description', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('titre_site', 'phone', 'email', 'copyright', 'date_add', 'date_update', 'status')
    search_fields = ('titre_site',)

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('icone', 'date_add', 'date_update', 'status')

@admin.register(models.Creative)
class CreativeAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('titre', 'progres','date_add', 'date_update', 'status')
    search_fields = ('titre',)
    
@admin.register(models.CardAbout)
class CardAboutAdmin(admin.ModelAdmin):
    list_display = ('icone','titre', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_add', 'date_update', 'status')
    search_fields = ('email',)

@admin.register(models.BannerContact)
class BannerContactAdmin(admin.ModelAdmin):
    list_display = ('imagecontact','titre', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

    def imagecontact(self,obj):
        return mark_safe(f'<img src= {obj.image.url} style= "width:100px; height:100px"')

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('job','nom', 'phone','date_add', 'date_update', 'status')
    search_fields = ('nom',)

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titre','sous_titre', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.AboutChoice)
class AboutChoiceAdmin(admin.ModelAdmin):
    list_display = ('imagechoice','titre','description', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)


    def imagechoice(self, obj):
        return mark_safe(f'<img src= {obj.image.url}style= "width:100px; height:100px"')

@admin.register(models.Icone)
class IconeAdmin(admin.ModelAdmin):
    list_display = ('nom','icone', 'date_add', 'date_update', 'status')
    search_fields = ('nom',)

@admin.register(models.ReseauSociaux)
class ReseauSociauxAdmin(admin.ModelAdmin):
    list_display = ('nom','icone', 'date_add', 'date_update', 'status')
    search_fields = ('nom',)

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('image','nom','job', 'date_add', 'date_update', 'status')
    search_fields = ('nom',)

    def image(self, obj):
        return mark_safe(f'<img src= {obj.image.url}style= "width:100px; height:100px"')
