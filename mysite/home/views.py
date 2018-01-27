from django.shortcuts import render, HttpResponseRedirect
from .forms import helpForm, taLogin

# Create your views here.
def index(request):
	return render(request, 'home/index.html')

def submit(request):
	if request.method == 'POST':
		form = helpForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/queue')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = helpForm()


	return render(request, 'home/submit.html', {'form': form})

def queue(request):
	return render(request, 'home/queue.html')

def tadash(request):
	return render(request, 'home/tadash.html')
	
def talogin(request):
	if request.method == 'POST':
		form = taLogin(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/dash')
	else:
		form = taLogin()
		
	return render(request, 'home/talogin.html', {'form': form})
			
		