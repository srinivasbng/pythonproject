from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Studentlogin
from .forms import For1,For
# Create your views here.
def index(request):
    return HttpResponse('HELLO WELCOME TO DJANGO')

def home(request):
    return render(request,'home.html')

def register(request):
    form=For(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        else:
            return HttpResponse('ERROR OCCURED')
    else:
        form=For()
        return render(request,'register.html',{'form':form})


def login(request):
    form=For1(request.POST)
    if request.method=='POST':
        if form.is_valid():
            a=form.cleaned_data['name']
            b=form.cleaned_data['eid']
            c=Student.objects.filter(name=a,eid=b)
            if not c:
                return HttpResponse('ERROR OCCURED')
            else:
                form=Studentlogin.objects.all()
                return render(request,'new.html',{'form':form})
    else:
        form=For1()
        return render(request,'login.html',{'form':form})


def walkins(request):
     return render(request,'walkins.html')


def students(request):
    form=Student.objects.filter()
    return render(request,'new.html',{'form':form})


def status(request):
    form=For1(request.POST)
    if request.method=='POST':
        if form.is_valid():
            a=form.cleaned_data['name']
            b=form.cleaned_data['eid']
            c=Student.objects.filter(name=a,eid=b)
            if not c:
                return HttpResponse('ERROR OCCURED')
            else:
                form=Student.objects.filter(name=a,eid=b)
                return render(request,'status.html')
    else:
        form=For1()
        return render(request,'login.html',{'form':form})
