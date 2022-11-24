from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models.functions import Lower
from .forms import VideoForm, SearchForm
from .models import Video


def home(request):
    app_name = 'Intreasts Videos'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

def add(request):

    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            try:
                new_video_form.save()
                return redirect('video_list')
                # messages.info(request, 'New Video Saved!')
            # todo give user input (success message or redirct)
            except ValidationError:
                messages.warning(request, 'Invalid YouTube URL')
            except IntegrityError:
                messages.warning(request, 'You have already added that video.')
        
        messages.warning(request, 'Please check the data entered.')
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

    new_video_form = VideoForm()

    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

def video_list(request):

    search_form = SearchForm(request.GET) # Build the form out of data the user has sent to app

    if search_form.is_valid():
        serach_term = search_form.cleaned_data['search_term']
        videos = Video.objects.filter(name__icontains=serach_term).order_by(Lower('name'))
    else: # Form is not valid or first time user sees the page.
        search_form = SearchForm()
        videos = Video.objects.order_by(Lower('name'))

    return render(request, 'video_collection/video_list.html', {'videos': videos, 'search_form': search_form})