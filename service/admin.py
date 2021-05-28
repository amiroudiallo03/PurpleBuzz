from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
# Register your models here.

@admin.register(models.BannerWork)
class BannerWorkAdmin(admin.ModelAdmin):
    list_display = ('titre','sous_titre', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.FuturedWork)
class FuturedWorkAdmin(admin.ModelAdmin):
    list_display = ('nom','titre', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('titre','sous_titre','imagepricing', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)


    def imagepricing(self,obj):
        return mark_safe(f'<img src= {obj.image.url} style="width: 100px; height: 100px"')

@admin.register(models.Pack)
class PackAdmin(admin.ModelAdmin):
    list_display = ('icone','titre','sous_titre','prix', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.Avantage)
class AvantageAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('titre',)

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('titre',)

@admin.register(models.CategorieWork)
class CategorieWorkAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('titre','sous_titre','categorie','imagecard', 'date_add', 'date_update', 'status')
    search_fields = ('titre',)

    def imagecard(self, obj):
        return mark_safe(f'<img src= {obj.image.url} style= "width:100px; height:100px"')


@admin.register(models.Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('titre','sous_titre','imagework','date_add', 'date_update', 'status')
    search_fields = ('titre',)

    def imagework(self, obj):
        return mark_safe(f'<img src= {obj.image.url} style= "width:100px; height:100px"')

