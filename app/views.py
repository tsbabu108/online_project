from django.shortcuts import render
from django.contrib import messages
from .models import Course

# Create your views here.
def index(request):
    return render(request,'index.html')


def adlogin(request):
    user=request.POST.get('t1')
    pwd=request.POST.get('t2')
    if user=='tsb' and pwd=='Babu1234':
        return render(request, 'admin_login.html', {'data':user})
    else:
        messages.info(request,'invalid user')
        return render(request,'index.html')


def schedule_class(request):
    return render(request,'addcourse.html')


def save(request):
    cname=request.POST.get('c1')
    faculty=request.POST.get('c2')
    cdate=request.POST.get('c3')
    c_time=request.POST.get('c4')
    fees=request.POST.get('c5')
    duratiion=request.POST.get('c6')
    try:
        Course(cname=cname,faculty=faculty,class_date=cdate,class_time=c_time,fees=fees,duration=duratiion).save()
        messages.info(request,'course add sucessfully')
        return render(request,'addcourse.html')
    except:
        messages.info(request,'something goeswrong')
        return render(request,'addcourse.html')