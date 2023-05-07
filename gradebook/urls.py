from django.urls import path
from . import views
from .views import SemesterList, SemesterCreate, SemesterUpdate, SemesterDelete, SemesterDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
    path("semester_list/", SemesterList.as_view(), name="semester_list"),
    path("semester_create/", SemesterCreate.as_view(), name="semester_create"),
    path("semester_update/<int:pk>/", SemesterUpdate.as_view(), name="semester_update"),
    path("semester_delete/<int:pk>/", SemesterDelete.as_view(), name="semester_delete"),
    path("semester_detail/<int:pk>/", SemesterDetail.as_view(), name="semester_detail"),
]
