from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home/index.html')

def submit(request):
	return render(request, 'home/submit.html')

def login(request):
	return render(request, 'home/TAlogin.html')