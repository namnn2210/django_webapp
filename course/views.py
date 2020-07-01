from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import Course
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# Create your views here.

@login_required
def all_courses(request):
    list_courses = {'courses': Course.objects.all().order_by('created_at')}
    return render(request, 'course/all_courses.html', list_courses)


@login_required
def created_updated(model, request):
    obj = model.objects.latest('pk')
    print(obj.user)
    if obj.user is None:
        obj.user = request.user
    obj.user = request.user
    obj.save()


@login_required
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            created_updated(Course, request)
            return redirect('/course/all')
    else:
        form = CourseForm()
    return render(request, 'course/add_course.html', {'form': form})


@login_required
def search_courses(request):
    if request.method == 'POST':
        search = request.POST['search']
        if search:
            match = Course.objects.filter(Q(title__icontains=search))
            if match:
                print(match)
                return render(request, 'course/all_courses.html', {'courses': match})
        else:
            return HttpResponseRedirect('course/all')
    return render(request, 'course/all_courses.html')


def get_courses_by_user(request):
    my_courses = Course.objects.filter(Q(user__username__iexact=request.user))
    return my_courses


@login_required
def edit_course(request, course_id):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = Course.objects.get(pk=course_id)
            course.updated_at = timezone.now()
            course_form = CourseForm(request.POST, instance=course)
            course_form.save()
            return redirect('profile')
    else:
        form = CourseForm(request.POST)
    return render(request, 'course/course_update.html', {'form': form})


@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return redirect('profile')
