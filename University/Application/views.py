from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import CreateView, View, DetailView, TemplateView
from .models import Department, Student, Instructor, Advisor, Course, Section
from django import forms


class DepartmentCreateView(CreateView):
    model = Department
    ctx = {'title': 'Add Department'}
    fields = ('dept_name', 'building', 'budget')


def IndexView(request):
    return render(request, 'static/index.html', {'name': 'Ajay Gunjal'})


class DepartmentDetailView(DetailView):
    model = Department
    # def get(self, request, *args, **kwargs):
    #     department = get_object_or_404(Department, pk=kwargs('pk'))
    #     context = {'department': department}
    #     return render(request, 'Application/department_detail', context)


class StudentCreateView(CreateView):
    model = Student
    fields = ('ID', 'firstName', 'lastName', 'dept_name', 'tot_cred')


class StudentDetailView(DetailView):
    model = Student


def allViews(request):
    # students = Student.objects.all()
    return render(request, 'Application/all-views.html', {})


class InstructorCreateView(CreateView):
    model = Instructor
    fields = ('ID', 'firstName', 'lastName', 'dept_name', 'salary')


class InstructorDetailView(DetailView):
    model = Instructor


class AdvisorCreateView(CreateView):
    model = Advisor
    fields = ('s_id', 'i_id')


class AdvisorDetailView(DetailView):
    model = Advisor


class CourseCreateView(CreateView):
    model = Course
    fields = ('course_id', 'title', 'dept_name', 'credits')


class CourseDetailView(DetailView):
    model = Course


class SectionCreateView(CreateView):
    model = Section
    fields = ('course_id', 'sec_id', 'semester', 'year')


class SectionDetailView(DetailView):
    model = Section

def StudentAllView(request):
    students = Student.objects.all()
    return render(request, 'Application/student_all_view.html', {'students': students})


def AdvisorAllView(request):
    advisors = Advisor.objects.all()
    return render(request, 'Application/advisor_all_view.html', {'advisors': advisors})


def CourseAllView(request):
    courses = Course.objects.all()
    return render(request, 'Application/course_all_view.html', {'courses': courses})


def DepartmentAllView(request):
    departments = Department.objects.all()
    return render(request, 'Application/department_all_view.html', {'departments': departments})


def InstructorAllView(request):
    instructors = Instructor.objects.all()
    return render(request, 'Application/instructor_all_view.html', {'instructors': instructors})


def SectionAllView(request):
    sections = Section.objects.all()
    return render(request, 'Application/section_all_view.html', {'sections': sections})