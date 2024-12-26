from django.shortcuts import render,HttpResponse
from home.models import Contact
def home(request):
    context={'name':'Anish','course':'django'}
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is my about page")
def projects(request):
    return render(request,'projects.html')
    # return HttpResponse("this is my projects page")
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        mesg=request.POST['mesg']
        print(name,email,phone,mesg)
        ins=Contact(name=name,email=email,phone=phone,mesg=mesg)
        ins.save()
        print("the data has been saved to the database")

    return render(request,'contact.html')
    # return HttpResponse("this is my contact page")
