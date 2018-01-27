from django.db import models

class TA(models.Model):
	#Properties of TA and the courses they teach
	taID = models.CharField(maxLength=20)
	taCode = models.CharField(maxLength=20)
	taCourses = models.ForeignKey(Course)
	#taCourses = models.ManyToManyField(Course)

class Course(models.Model):
	#has identifying code/name and list of TA's for the course
	courseName = models.CharField(maxLength=20)
	courseCode = models.CharField(maxLength=20)
	courseTas = models.ForeignKey(TA)
	#courseTAs = models.ManyToManyField(TA)

class Student(models.Model):
	#has identifying properties so they can be contacted
	studentName = models.CharField(maxLength=30)
	studentID = models.CharField(maxLength=20)
	studentEmail = models.CharField(maxLength=50)
	studentPhone= models.Charfield(maxLength=20)

class Queue(models.Model):
	#has TA, course and student
	queueSize = models.IntegerField()
	ta = models.ManyToManyField(TA)
	students = models.ForeignKey(Student, on_delete=models.CASCADE)