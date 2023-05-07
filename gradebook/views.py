from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Student
from .models import StudentEnrollment
from .models import Lecturer
from .models import Class

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'students': Student.objects.all()
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

