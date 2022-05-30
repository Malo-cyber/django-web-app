from django.contrib import admin
from listings.models import Band, Listing

# Register your models here.

class BandAdmin(admin.ModelAdmin):  # class pour afficher plus d'information en admin
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

class ListingAdmin(admin.ModelAdmin):  # class pour afficher plus d'information en admin
    list_display = ('title', 'sold', 'description','band') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument

admin.site.register(Listing, ListingAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument