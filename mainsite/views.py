from django.shortcuts import render, redirect
from mainsite import models, forms
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import EmailMessage


# Create your views here.
def index(request):
    if 'username' in request.session:
        username = request.session['username']
        # useremail = request.session['username']
    job_list = models.Job_list.objects.all()
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html', locals())


def detail(request, jobID):
    job_detail = models.Job_list.objects.get(id=jobID)
    if 'username' in request.session:
        name = request.session['username']
        department = request.session['department']
        email = request.session['email']
    return render(request, 'detail.html', locals())


def category(request):
    try:
        profession = request.GET['profession']
        location = request.GET['location']
    except:
        pass

    result = models.Job_list.objects.filter(skill__iexact=profession) | models.Job_list.objects.filter(
        location__iexact=location)
    count = len(result) + 1
    return render(request, 'category.html', locals())


def register(request):
    form = forms.ContactForm()
    return render(request, 'register.html', locals())


def test(request):
    if 'username' in request.session:
        name = request.session['username']
        department = request.session['department']
        email = request.session['email']
    return render(request, 'test.html', locals())


def apply(request):
    if 'username' in request.session:
        name = request.session['username']
        department = request.session['department']
        email = request.session['email']
    return render(request, 'apply.html', locals())

def message(request):
    messages = request.POST['message'].strip()
    return render(request, 'message.html', locals())

def send(request):
    title = '你有來自高師徵才網的求職信'
    apply_name = request.POST['apply_name'].strip()
    apply_department = request.POST['apply_department'].strip()
    apply_description = request.POST['apply_description'].strip()
    apply_email = request.POST['apply_email'].strip()
    JobID = request.POST['JobID'].strip()
    job_detail = models.Job_list.objects.get(id=JobID)
    company_email = job_detail.company_email.strip()
    print(company_email)

    email = EmailMessage(title, apply_description, apply_email, [company_email])
    email.send()
    return render(request, 'message.html', locals())


def login(request):
    if request.method == 'POST':
        login_acc = request.POST['useracc'].strip()
        login_password = request.POST['password']
        try:
            user = models.User.objects.get(account=login_acc)
            if user.password == login_password:
                request.session['username'] = user.name
                request.session['department'] = user.department
                request.session['email'] = user.email
                return redirect('/')
            else:
                messages = "密碼錯惹啦!"
        except:
            messages = "找不到使用者"
    else:
        login_form = forms.LoginForm()
    return render(request, 'index.html', locals())


@csrf_exempt
def logout(request):
    request.session['username'] = None
    return HttpResponse('成功登出')


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
