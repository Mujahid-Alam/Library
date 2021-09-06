
from django.contrib import admin
from django.urls import path
from datawork.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dashboard,name="dashboard"),
    path('manage-students/',manage_students,name="manage_student"),
    path('add-students/',add_student,name="add_student"),
    path('manage-books/',manage_books,name="manage_books"),
    path('add-books/',add_books,name="add_books"),
    path('add-entry/',add_entry,name="add_entry"),
    path('manage-orders/',manage_orders,name="manage_orders"),
    path('active-orders',active_orders,name="active_orders"),
    path('book/delete/<int:id>/',deleteBook,name="delete_book"),
    path('studnet/delete/<int:id>/',deleteStudent,name="delete_student")
    
]
