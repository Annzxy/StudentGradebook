from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Student, StudentEnrollment, Lecturer, Class, Semester
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