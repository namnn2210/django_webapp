from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    url = forms.URLField(max_length=200, required=True)

    class Meta:
        model = Course
        fields = ['title', 'url']
