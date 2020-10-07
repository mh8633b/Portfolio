from django.shortcuts import render

# Create your views here.
from muneebulhassan.models import project, experience, experiencedetail, connect


def index(request):
    if(request.method=="POST"):
        name = request.POST.get('name','')
        subject = request.POST.get('subject','')
        email = request.POST.get('email','')
        cnt = connect(u_name=name, u_subject=subject , u_email=email)
        cnt.save()
        # print(request)
    projects = project.objects.all
    exp = experience.objects.all
    expd = experiencedetail.objects.all()
    parms ={'project' : projects, 'experience': exp, 'exp_detail' : expd }
    return render(request, "index.html",parms)




# def add(request):
#     name = request.GET['username']
#     project = request.GET['project']
#     print(name + "  this is pasd " + project)
#     return render(request, "index.html")
