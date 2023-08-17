
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", views.StudentView.as_view(), name="add_student"),
    path('students/', views.GetAllStudentView.as_view()),
    path('student_detail/<int:id>/', views.StudentDetailView.as_view(), name="view_student_detail"),
    path('delete_student/<int:id>/', views.DeleteStudentView.as_view(), name="delete-student"),
    path('update_student/<int:id>/', views.UpdateStudentView.as_view(), name="update-student")
]
