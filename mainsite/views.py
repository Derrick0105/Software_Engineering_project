from django.shortcuts import render,redirect
from mainsite import models,forms
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
def index(request):
    if 'username' in request.session:
        username=request.session['username']
        #useremail = request.session['username']
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

def register(request):
    form = forms.ContactForm()
    return  render(request,'register.html',locals())

def login(request):
    if request.method == 'POST':
        login_acc=request.POST['useracc'].strip()
        login_password=request.POST['password']
        try:
            user=models.User.objects.get(account=login_acc)
            if user.password==login_password:
                request.session['username']=user.name
                request.session['email'] = user.email
                return redirect('/')
            else:
                messages="密碼錯惹啦!"
        except:
            messages="找不到使用者"
    else:
        login_form = forms.LoginForm()
    return render(request, 'index.html', locals())
@csrf_exempt
def logout(request):
    request.session['username'] = None
    return HttpResponse('成功登出')

def test(request):
    te=request.session['password']
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
