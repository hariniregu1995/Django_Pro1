from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'student_name']
        widgets = {
            'course_name': forms.TextInput(attrs={'class':'form-control'}),
            'student_name': forms.TextInput(attrs={'class':'form-control'}),
        }
