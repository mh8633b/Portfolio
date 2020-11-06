from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
import requests
import itertools


# Create your views here.
from muneebulhassan.models import project, experience, experiencedetail, connect


def index(request):
    # if(request.method=="POST"):
    #     name = request.POST.get('name','')
    #     subject = request.POST.get('subject','')
    #     email = request.POST.get('email','')
    #     cnt = connect(u_name=name, u_subject=subject , u_email=email)
    #     cnt.save()
    #     send_mail("abc","asdasdad", 'mh8633b@gmail.com',['monybluex@gmail.com'])
    #

    # repo_list_url =
    repo = requests.get("https://api.github.com/users/monybluex/repos")
    repo_data = repo.json()
    projects = project.objects.all
    exp = experience.objects.all
    expd = experiencedetail.objects.all()
    for data in repo_data:
        print(data['name'])
    parms ={'project' : projects, 'experience': exp, 'exp_detail' : expd, 'repos' : repo_data }
    return render(request, "index.html",parms)
