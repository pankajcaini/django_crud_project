from django.shortcuts import render, HttpResponse, redirect
from app.forms import NewStudentForm
from django.views import View
from app.models import Student



class StudentView(View):
    template = 'new_student.html'
    def get(self, request):
        form = NewStudentForm()
        return render(request, self.template, {'form':form})


    def post(self, request):
        form = NewStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data saved")
        else:
            return render(request, self.template, {'form':form})
        


class GetAllStudentView(View):
    template = 'all_students.html'
    def get(self, request):
        students = Student.objects.all()
        return render(request, self.template, {'students':students})



class StudentDetailView(View):
    template = 'student_detail.html'
    def get(self, request, id):
        student = Student.objects.get(pk=id)
        context = {'student':student}
        return render(request, self.template,context)
    

class DeleteStudentView(View):
    def get(self, request,id):
        student = Student.objects.get(pk=id)
        student.delete()
        return redirect('/students/')
    


class UpdateStudentView(View):
    template = 'update_student.html'
    def get(self, request,id):
        student = Student.objects.get(pk=id)
        form = NewStudentForm(instance=student)
        context = {'form':form}
        return render(request, self.template, context)
    
    def post(self, request, id):
        student = student = Student.objects.get(pk=id)
        form = NewStudentForm(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/students/')
        else:
            return render(request, self.template, {'form':form})