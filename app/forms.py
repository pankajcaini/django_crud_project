from django import forms
from app.models import Student

class NewStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

