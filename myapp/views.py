from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm

# Home page
def home(request):
    return render(request, 'home.html')

# Add Course
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_courses')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

# View Courses
def view_courses(request):
    courses = Course.objects.all()
    return render(request, 'view_courses.html', {'courses': courses})
