from django.contrib import admin

from .models import TA
admin.site.register(TA)

from .models import Course
admin.site.register(Course)

from .models import Student
admin.site.register(Student)

from .models import Queue
admin.site.register(Queue)
