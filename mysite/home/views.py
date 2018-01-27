from django.shortcuts import render, HttpResponseRedirect
from .forms import helpForm

# Create your views here.
def index(request):
	return render(request, 'home/index.html')

def submit(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = helpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/queue')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = helpForm()

    return render(request, 'home/submit.html', {'form': form})

def queue(request):
	return render(request, 'home/queue.html')

def tadash(request):
	return render(request, 'home/tadash.html')
	