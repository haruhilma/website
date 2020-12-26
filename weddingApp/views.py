from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.

def Home(request):

    banner = Slider.objects.order_by('-id')[0]
    story = Setings.objects.order_by('-id')[0]
    cat = CategoryEvent.objects.all().order_by('id')
    event = Event.objects.all().order_by('id')[:2]
    gallery = Gallery.objects.all().order_by('id')
    return render(request, 'home.html', {'banner' : banner, 'story' : story,'event' : event,'cat' : cat,'gallery' : gallery})

def invitation(request):
    name=request.POST['name']
    relation=request.POST['relation']
    email=request.POST['email']

    qr = Invitations(invitation_tamu = name,invitation_pasangan_tamu = relation,invitaion_email = email)
    qr.save()

    return HttpResponse('<script> alert("Anda Berhasil Melakukan reservasi"); window.location = "/"; </script>')



