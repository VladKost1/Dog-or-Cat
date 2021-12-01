from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Animal, Photo
from .utils import recognize_animal


def index(request):
    if request.method == 'GET':
        return render(request, 'main/index.html')
    new_photo = Photo(img=request.FILES['pht'])
    new_photo.save()
    return redirect(reverse('recognize', kwargs={'photo_id': new_photo.id}))


def recognize(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    slug = recognize_animal(path=photo.img.url)

    return render(request, 'main/result.html', context={'animal': slug, 'photo': photo.img.url})

