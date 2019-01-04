from django.shortcuts import render
from mainsite import models
# Create your views here.
def index(request):
    job_list=models.Job_list.objects.all()
    return render(request,'index.html',locals())

def about(request):
    return render(request,'about.html',locals())