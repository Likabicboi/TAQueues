from django.db import models
from django.forms import ModelForm

class Student(models.Model):
	#has identifying properties so they can be contacted
	studentName = models.CharField(max_length=30)
	studentID = models.CharField(max_length=20)
	studentIssue = models.CharField(max_length=200)
	studentEmail = models.CharField(max_length=50)
	studentPhone= models.CharField(max_length=20)

	def __str__(self):
		return self.studentName

class TA(models.Model): #Courses taught + need mulitple fucntionality

	#Properties of TA and the courses they teach
	taID = models.CharField(max_length=20)
	taCode = models.CharField(max_length=20)
	taName = models.CharField(max_length=30)
	#currentStudent = models.CharField(max_length=30, default='')
	currentStudent = models.CharField(max_length=30, null = True, blank = True)
	taCourses = []

	#Check whether current student can be blank

	def __str__(self):
		return self.taName
	def addTACourse(courseAdding):
		taCourses.append(courseAdding)
	def removeTACourse(courseDropping):
		taCourses.remove(courseDropping)

	#taCourses = models.ManyToManyField(Course)

class Queue(models.Model):
	#has TA, course and student
	queueSize = models.IntegerField(default=0, blank = True,  null = True)
	students = models.ForeignKey(Student, null = True, blank = True, on_delete=models.CASCADE)

	"""def __str__(self):
		return "Queue for: " % course"""
	def addtoQueue(x):
		students.append(x)
	def deQueue():
		return students.pop(0)


class Course(models.Model):
	#has identifying code/name and list of TA's for the course
	courseNum = models.CharField(max_length=20)
	courseCode = models.CharField(max_length=20)
	courseTAs = models.ManyToManyField(TA)
	queue = models.ManyToManyField(Queue)
	def __str__(self):
		return self.courseNum
	#courseTas = models.ForeignKey(TA)
	#availableTAs = models.ManyToManyField(TA)


#Forms for each database created (possibly irrelevant)

"""class TAForm(ModelForm):
	class Meta:
		model = TA
		fields = ['taID', 'taCode', 'taName', 'currentStudent']

class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ['courseNum', 'courseCode', 'courseTAs', 'queue']

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['studentName', 'studentID', 'studentIssue', 'studentEmail', 'studentPhone']

class QueueForm(ModelForm):
	class Meta:
		model = Queue
		fields = ['queueSize', 'students']"""

		