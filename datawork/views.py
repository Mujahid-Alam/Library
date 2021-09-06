from django.shortcuts import *
from datawork.models import *
from datawork.forms import *

# Create your views here.


def dashboard(r):
    return render(r,"home.html")


def manage_students(r):
    data = {"students":User.objects.filter(is_superuser=False)}
    return render(r,"manage_students.html",data)
    
   


def add_student(r):
     form = StudentForm(r.POST or None)
     data = {"form":form}
     if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("manage_student")
        else:
            return render(r,"add_student.html",data)
     return render(r,'add_student.html',data)
 
def deleteStudent(r,id):
    User.objects.get(id=id).delete()
    return redirect("manage_student")

def deleteBook(r,id):
    Book.objects.get(id=id).delete()
    return redirect("manage_books")

def manage_books(r):
    data = {"books":Book.objects.all()}
    return render(r,'manage_books.html',data)


def add_books(r):
    form = BookForm(r.POST or None)
    
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('manage_books')
        else:
            return render(r,"add_books.html",{"form":form})
    else:
        return render(r,'add_books.html',{"form":form})
        
        
def add_entry(r):
    return render(r,'add_entry.html')

def orders(r):
    return render(r,'orders.html')

def active_orders(r):
    return render(r,'active_orders.html')

def manage_orders(r):
    return render(r,'manage_orders.html')