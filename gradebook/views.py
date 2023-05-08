from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Student, StudentEnrollment, Lecturer, Class, Semester, Course
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'students': Student.objects.all()
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

class SemesterList(ListView):
    model = Semester
    template_name = "Semester_List.html"

class SemesterCreate(CreateView):
    model = Semester
    template_name = "Semester_Create.html"
    fields = "__all__"
    success_url = reverse_lazy("semester_list")

class SemesterUpdate(UpdateView):
    model = Semester
    template_name = "Semester_Update.html"
    fields = "__all__"
    success_url = reverse_lazy("semester_list")

class SemesterDetail(DetailView):
    model = Semester
    template_name = "Semester_Detail.html"

class SemesterDelete(DeleteView):
    model = Semester
    template_name = "Semester_Delete.html"
    success_url = reverse_lazy("semester_list")

class CourseList(ListView):
    model = Course
    template_name = "Course_List.html"

class CourseCreate(CreateView):
    model = Course
    template_name = "Course_Create.html"
    fields = "__all__"
    success_url = reverse_lazy("course_list")

class CourseUpdate(UpdateView):
    model = Course
    template_name = "Course_Update.html"
    fields = "__all__"
    success_url = reverse_lazy("course_list")

class CourseDetail(DetailView):
    model = Course
    template_name = "Course_Detail.html"

class CourseDelete(DeleteView):
    model = Course
    template_name = "Course_Delete.html"
    success_url = reverse_lazy("course_list")

class LecturerList(ListView):
    model = Lecturer
    template_name = "Lecturer_List.html"

class LecturerCreate(CreateView):
    model = Lecturer
    template_name = "Lecturer_Create.html"
    fields = "__all__"
    success_url = reverse_lazy("lecturer_list")

class LecturerUpdate(UpdateView):
    model = Lecturer
    template_name = "Lecturer_Update.html"
    fields = "__all__"
    success_url = reverse_lazy("lecturer_list")

class LecturerDetail(DetailView):
    model = Lecturer
    template_name = "Lecturer_Detail.html"

class LecturerDelete(DeleteView):
    model = Lecturer
    template_name = "Lecturer_Delete.html"
    success_url = reverse_lazy("lecturer_list")

class ClassList(ListView):
    model = Class
    template_name = "Class_List.html"

class ClassCreate(CreateView):
    model = Class
    template_name = "Class_Create.html"
    fields = "__all__"
    success_url = reverse_lazy("class_list")

class ClassUpdate(UpdateView):
    model = Class
    template_name = "Class_Update.html"
    fields = "__all__"
    success_url = reverse_lazy("class_list")

class ClassDetail(DetailView):
    model = Class
    template_name = "Class_Detail.html"

class ClassDelete(DeleteView):
    model = Class
    template_name = "Class_Delete.html"
    success_url = reverse_lazy("class_list")