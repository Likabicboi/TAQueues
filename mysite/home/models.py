from django.db import models
from django.forms import ModelForm

class Student(models.Model):
	#has identifying properties so they can be contacted
	studentName = models.CharField(max_length=30)
	studentID = models.CharField(max_length=20)
	studentEmail = models.CharField(max_length=50)
	studentPhone= models.CharField(max_length=20)

class TA(models.Model):
	#Properties of TA and the courses they teach
	taID = models.CharField(max_length=20)
	taCode = models.CharField(max_length=20)
	taName = models.CharField(max_length=30)
	currentStudent = models.CharField(max_length=30, default='')
	#taCourses = models.ForeignKey(Course)
	#taCourses = models.ManyToManyField(Course)

class Course(models.Model):
	#has identifying code/name and list of TA's for the course
	courseName = models.CharField(max_length=20)
	courseCode = models.CharField(max_length=20)
	#courseTas = models.ForeignKey(TA)
	courseTAs = models.ManyToManyField(TA)
	#availableTAs = models.ManyToManyField(TA)

class Queue(models.Model):
	#has TA, course and student
	queueSize = models.IntegerField(default=0, blank = True,  null = True)
	course = models.ManyToManyField(Course)
	students = models.ForeignKey(Student, on_delete=models.CASCADE)

#Forms for each database created (possibly irrelevant)

class TAForm(ModelForm):
	class Meta:
		model = TA
		fields = ['taID', 'taCode', 'taName', 'currentStudent']

class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ['courseName', 'courseCode', 'courseTAs']

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['studentName', 'studentID', 'studentEmail', 'studentPhone']

class QueueForm(ModelForm):
	class Meta:
		model = Queue
		fields = ['queueSize', 'course', 'students']