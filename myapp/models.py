from django.db import models
from datetime import date

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    enrollment_date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.course_name} - {self.student_name}"

    class Meta:   
        db_table = 'user'   
        
