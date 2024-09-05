from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    projects_show=[
        {
            "title":"RMS Project",
            "path":"img/RMS_proj.png",
        },
         {
            "title":"Portfolio",
            "path":"img/Shrey_portfolio.png",
        },
        {
            "title":"Ecommerce",
            "path":"img/ecommerce.png",
        },
        {
            "title":"Timetable Schedular",
            "path":"img/timtable.png",
        },
         {
            "title":"CRUD",
            "path":"img/CRUD.png",
        },
          {
            "title":"Photo Uploader",
            "path":"img/photo_uploader.png",
        },
        {
            "title":"To do list",
            "path":"img/todolist.png",
        },
        {
            "title":"Labour Hiring",
            "path":"img/labour_hiring.png",
        },
    ]
    return render(request,"projects.html",{"projects_show":projects_show})
 
# def experience(request):
#     return render(request,'experience.html')

def certification(request):
    return render(request,'certification.html')

def contact(request):
    return render(request,'contact.html')

def resume(request):
    resume_path="img/My_Resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content.Disposition']='attachment';filename="My_Resume.pdf"
            return response
    else:
        return HttpResponse("resume not found",status=404)