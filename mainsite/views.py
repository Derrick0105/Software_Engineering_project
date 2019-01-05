from django.shortcuts import render
from mainsite import models
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
def index(request):
    job_list = models.Job_list.objects.all()
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html', locals())


def detail(request, jobID):
    job_detail = models.Job_list.objects.get(id=jobID)
    return render(request, 'detail.html', locals())

def category(request):
    try:
        profession = request.GET['profession']
        location = request.GET['location']
    except:
        pass

    result = models.Job_list.objects.filter(skill__iexact=profession) | models.Job_list.objects.filter(
        location__iexact=location)
    count=len(result)+1
    return  render(request,'category.html',locals())

def test(request):
    return  render(request,'test.html',locals())
'''
@csrf_exempt
def searching(request):
    profession=request.POST.get('profession')
    location=request.POST.get('location')
    result = models.Job_list.objects.filter(skill__iexact=profession)| models.Job_list.objects.filter(
    location__contains=location)
    id_list=[]
    for i in result:
        id_list.append(i.id)

    return HttpResponse(id_list)
'''
