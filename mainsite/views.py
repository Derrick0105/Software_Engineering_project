from django.shortcuts import render
from mainsite import models
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    job_list = models.Job_list.objects.all()
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html', locals())


def detail(request, jobID):
    job_list = models.Job_list.objects.all()
    job_detail = job_list[jobID]
    return render(request, 'detail.html', locals())

@csrf_exempt
def searching(request):
    profession=request.POST.get('profession')
    location=request.POST.get('location')
    result = models.Job_list.objects.filter(skill__iexact=profession)| models.Job_list.objects.filter(
    location__contains=location)
    return HttpResponseRedirect("/about")

