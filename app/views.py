from django.shortcuts import render
from . models import Student
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import StudentForm



# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = '/'


class StudentListView(ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student


class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'app/student_update.html'
    success_url = '/'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/'


def student_form(request):
    form = StudentForm()
    return render(request,'app/form.html',{'form':form})