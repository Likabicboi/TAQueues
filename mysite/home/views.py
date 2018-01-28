from django.shortcuts import render, HttpResponseRedirect
from .forms import helpForm, taLogin
from .models import Course, Student
from django.http import Http404
from django.contrib import messages

# Create your views here.
def index(request):
	classes = Course.objects.all()
	
	return render(request, 'home/index.html', {'classes': classes})

def submit(request, oid):

	for course in Course.objects.all():
		if course.courseNum == oid:
			currentCourse = course
			break
			
	

	if request.method == 'POST':
		form = helpForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			issue = form.cleaned_data['issue']
			student_id = form.cleaned_data['student_id']
			email = form.cleaned_data['email']
			number = form.cleaned_data['number']
			passcode = form.cleaned_data['passcode']

			# Checks if the course's code matches that of the passcode given
			if currentCourse.courseCode == passcode:
				s = Student(studentName = name, studentID = student_id, studentIssue = issue, studentEmail = email, studentPhone = number)
				s.save()
				return HttpResponseRedirect('/queue/'+student_id)
			else:
				form = helpForm()
				messages.error(request, 'Invalid class code.')

  # if a GET (or any other method) we'll create a blank form
	else:
		form = helpForm()

	args = {'form': form, 'course':currentCourse}
	return render(request, 'home/submit.html', args)

def queue(request, id):
	current = None
	for student in Student.objects.all():
		if student.studentID == id:
			current = student
			break
	
	if current == None:
		raise Http404
	return render(request, 'home/queue.html', {'student': current})

def tadash(request):
	return render(request, 'home/tadash.html')
	
def talogin(request):
	if request.method == 'POST':
		form = taLogin(request.POST)
		if form.is_valid():
			student_id = form.cleaned_data['student_id']
			passcode = form.cleaned_data['passcode']

			if TA.objects.filter(taID=student_id).exists(): 
				return HttpResponseRedirect('/dash')
			else:
				print("Invalid")
			
	else:
		form = taLogin()
		
	return render(request, 'home/talogin.html', {'form': form})
			
		