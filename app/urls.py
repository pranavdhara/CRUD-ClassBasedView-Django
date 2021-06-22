from django.urls import path,include

from . views import StudentCreateView,StudentListView,StudentDetailView,StudentUpdateView,StudentDeleteView,student_form
urlpatterns = [
    
    path('create', StudentCreateView.as_view(), name='stu-create' ),
    path('', StudentListView.as_view(), name='stu-list' ),
    path('list/<pk>', StudentDetailView.as_view(), name='stu-detail' ),
    path('update/<pk>', StudentUpdateView.as_view(), name='stu-update' ),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='stu-delete' ),
    # path('<pk>/', StudentDetailView.as_view()),
    path('form', student_form, name='stu-form' ),
]
