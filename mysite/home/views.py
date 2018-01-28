from django.shortcuts import render, HttpResponseRedirect
from .forms import helpForm, taLogin
from .models import Course, Student, TA
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

def tadash(request, tid):
	current = None
	for ta in TA.objects.all():
		if tid == ta.taEmail:
			current = ta
			break

	args = {'ta':current}
	

	return render(request, 'home/tadash.html', args)
	
def talogin(request):
	if request.method == 'POST':
		form = taLogin(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			passcode = form.cleaned_data['passcode']

			for ta in TA.objects.all():
				if email == ta.taEmail:
					if passcode == ta.taCode:
						return HttpResponseRedirect('/dash/'+email)
					else:
						messages.error(request, 'Invalid password. Try again.')
	else:
		form = taLogin()
		
	return render(request, 'home/talogin.html', {'form': form})
			
		