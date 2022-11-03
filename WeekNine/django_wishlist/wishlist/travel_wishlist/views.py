from django.shortcuts import render, redirect
from .models import Place
from .forms import NewPlaceForm


def place_list(request):

    if request.method == 'POST':
        # create a new place
        form = NewPlaceForm(request.POST) # Creating form from data in the request.
        place = form.save() # creating a model object from form
        if form.is_valid():  # validation against DB constraints
            place.save() # saves place to DB
            return redirect('place_list') # reloads home page

    # Runs if it is a get request.
    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm() # Used to create for html
    return render(
        request, 
        'travel_wishlist/wishlist.html', 
        {'places': places, 'new_place_form': new_place_form})

def about(request):
    author = 'Nate O'
    about = 'A website to create a list of places I would like to visit.'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})