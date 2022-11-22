from django.shortcuts import render
from django.contrib import messages
from .forms import VideoForm


def home(request):
    app_name = 'Intreasts Videos'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

def add(request):

    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            new_video_form.save()
            messages.info(request, 'New Video Saved!')
            # todo give user input (success message or redirct)
        else:
            messages.warning(request, 'Please check the data entered.')
            return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

    new_video_form = VideoForm()

    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})