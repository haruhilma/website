from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.

class Slider(models.Model):
    slider_title=models.CharField(max_length=255)
    slider_images = models.ImageField(upload_to='slider/') 
    slider_description=models.TextField()
    slider_created_by=models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    slider_created_at=models.DateTimeField(auto_now_add=True)

    def __set__(self):
        return self.slider_title

    def images(self):
        if self.slider_images:
            return mark_safe('<img src="/upload/%s" width="150" height="100" />' %(self.slider_images))

    def bannerFront(self):
        if self.slider_images:
            return mark_safe('<img src="/upload/%s" />' %(self.slider_images))

class CategoryEvent(models.Model):
    kategori_title=models.CharField(max_length=255)
    kategori_description=models.TextField()
    kategori_created_by=models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    kategori_created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Kategori"

    def __str__(self):
        return self.kategori_title

    def __set__(self):
        return self.kategori_title

class Event(models.Model):
    event_title=models.CharField(max_length=255)
    event_id_kategori=models.ForeignKey(CategoryEvent, verbose_name="Kategori" ,related_name="kategori", on_delete=models.CASCADE)
    event_images = models.ImageField(upload_to='event/') 
    event_description=models.TextField()
    event_location=models.CharField(max_length=255)
    event_shedule=models.DateTimeField(auto_now_add=False)
    event_created_by=models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    event_created_at=models.DateTimeField(auto_now_add=True)

    def __set__(self):
        return self.event_title

    def eventImages(self):
        if self.event_images:
            return mark_safe('<img src="/upload/%s" width="150" height="100" />' %(self.event_images))
    
    def eventImagesFront(self):
        if self.event_images:
            return mark_safe('<img src="/upload/%s" class="accordion__item-img" />' %(self.event_images))

class Gallery(models.Model):
    gallery_title=models.CharField(max_length=255)
    gallery_images = models.ImageField(upload_to='gallery/') 
    gallery_description=models.TextField()
    gallery_created_by=models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    gallery_created_at=models.DateTimeField(auto_now_add=True)

    def __set__(self):
        return self.gallery_title

    def images(self):
        if self.gallery_images:
            return mark_safe('<img src="/upload/%s" width="150" height="100" />' %(self.gallery_images))

    def imagesFront(self):
        if self.gallery_images:
            return mark_safe('<img src="/upload/%s" lt="slider" />' %(self.gallery_images))


class Setings(models.Model):
    setting_nama_pria = models.CharField('Nama Mempelai Pria', max_length=255)
    setting_nama_perempuan = models.SlugField('Nama Mempelai Perempuan', max_length=255, unique=True)
    setting_schedule=models.DateTimeField(auto_now_add=False)
    setting_location=models.CharField(max_length=255)
    setting_email=models.CharField(max_length=255)
    setting_contact=models.CharField(max_length=255)
    setting_footer_title=models.CharField(max_length=255)
    setting_footer_content=models.TextField()
    setting_story_content=models.TextField()


class Invitations(models.Model):
    invitation_tamu = models.CharField('Nama Tamu', max_length=255)
    invitation_pasangan_tamu = models.CharField('Nama Rekan Tamu', max_length=255, unique=True)
    invitaion_email=models.CharField('E-mail',max_length=255)
    
