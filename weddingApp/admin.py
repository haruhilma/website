from django.contrib import admin
from .models import *
from django.db.models import Count

#custom table admin kategori event
class CategoryEventAdmin(admin.ModelAdmin):
    sortable_by = 'kategori_title'
    search_fields = ['kategori_title']
    list_display = ('kategori_title','kategori_description','kategori_created_by','kategori_created_at')
    list_display_links = ('kategori_title',)

    fieldsets = [
        (None, { 'fields': [('kategori_title','kategori_description')] } ),
    ]

    def kategori_created_by(self, obj):
        return obj.username
    kategori_created_by.short_description ='Created'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'slider_created_by', None) is None:
            obj.kategori_created_by = request.user
        obj.save()

class SliderAdmin(admin.ModelAdmin):
    sortable_by = 'slider_title'
    search_fields = ['slider_title']
    list_display = ('images','slider_title','slider_description','slider_created_by','slider_created_at')
    list_display_links = ('slider_title',)
    fieldsets = [
        (None, { 'fields': [('slider_title','slider_images','slider_description','slider_created_by')] } ),
    ]

    def slider_created_by(self, obj):
        return obj.username
    slider_created_by.short_description ='Created'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'slider_created_by', None) is None:
            obj.slider_created_by = request.user
        obj.save()

class EventAdmin(admin.ModelAdmin):
   

    sortable_by = 'id'
    search_fields = ['event_title']
    list_display = ('eventImages','event_title','event_id_kategori','event_location','event_shedule','event_description','event_created_by','event_created_at')
    list_display_links = ('event_title',)

    fieldsets = [
        (None, { 'fields': [('event_title','event_id_kategori','event_images','event_description','event_location','event_shedule')] } ),
    ]

    def event_created_by(self, obj):
        return obj.username
    event_created_by.short_description ='Created'

    def event_id_kategori(self, obj):
        return obj.kategori_title
    event_id_kategori.short_description ='Kategori Event'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'event_created_by', None) is None:
            obj.event_created_by = request.user
        obj.save()

class GalleryAdmin(admin.ModelAdmin):
    sortable_by = 'gallery_title'
    search_fields = ['gallery_title']
    list_display = ('images','gallery_title','gallery_description','gallery_created_by','gallery_created_at')
    list_display_links = ('gallery_title',)
    fieldsets = [
        (None, { 'fields': [('gallery_title','gallery_images','gallery_description')] } ),
    ]

    def gallery_created_by(self, obj):
        return obj.username
    gallery_created_by.short_description ='Created'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'gallery_created_by', None) is None:
            obj.gallery_created_by = request.user
        obj.save()


class SettingsAdmin(admin.ModelAdmin):

    def get_total(self):
        #functions to calculate whatever you want...
        total = Setings.objects.all().aggregate(tot=Count('id'))['tot']
        return total


    def has_add_permission(self, request):
        if(self.get_total() > 0):
            return False
        else:
            return True
            
    list_display = ('setting_nama_pria','setting_nama_perempuan','setting_schedule','setting_location','setting_email','setting_contact')

class InvitationsAdmin(admin.ModelAdmin):
            
    list_display = ('invitation_tamu','invitation_pasangan_tamu','invitaion_email')

#custom title bar admin
admin.site.site_title = 'Wedding Admin Pages'
admin.site.site_header = 'Admin Dasboard'

# Register your models here.
admin.site.register(Slider,SliderAdmin)
admin.site.register(CategoryEvent,CategoryEventAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Gallery,GalleryAdmin)

admin.site.register(Setings, SettingsAdmin)

admin.site.register(Invitations,InvitationsAdmin)

