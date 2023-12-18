from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import IntegrateForm , BotSettingForm ,AppSettingForm,  CompanyForm, CompanyEditForm, ProfileForm, AppSettingEditForm
import openai
from .models import BotSetting, AppSetting, User , AddUser, AddUserProfile ,FbIntegrate, AddCompany, Chat
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone





def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        lname = request.POST['lname']
        fname = request.POST['fname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        img = request.FILES.get('img')

        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, email=email,password= password1, first_name=fname ,last_name =lname, user_image=img) 
                user.save()
                auth.login(request, user)
                return redirect('chat:login')
            except:
                error_message = 'Error creating account'
                return render(request, 'chat/register/signup.html', {'error_message': error_message})
            
       
        else:
            error_message = 'Password dont match'
            return render(request, 'chat/register/signup.html', {'error_message': error_message})
        
        
    return render(request, 'chat/register/signup.html')


def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        lname = request.POST['lname']
        fname = request.POST['fname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        img = request.FILES.get('img')
        user_id = request.POST['user_id']



        if password1 == password2:
            try:
                user = AddUser.objects.create_user(username=username,email=email,password=password1, first_name=fname,last_name = lname,user_image=img, user_id=user_id)
                user.save()
                return redirect('chat:home')
            except:
                error_message = 'Error creating account'
                return render(request, 'chat/pages/add_user.html', {'error_message': error_message})
            
        else:
            error_message = 'Password dont match'
            return render(request, 'chat/pages/add_user.html', {'error_message': error_message})
        
        
    return render(request, 'chat/pages/add_user.html',)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chat:home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'chat/register/login.html', {'error_message': error_message})
    else:
        return render(request, 'chat/register/login.html')


def logout(request):
    auth.logout(request)
    return redirect('chat:login')

def forgot(request):
    return render(request, 'chat/register/forgot.html')

# @login_required(login_url="/login")
def home(request):
    appset = AppSetting.objects.filter(user_id= request.user.id)
    user = AddUser.objects.filter(user_id = request.user.id)
    return render(request, "chat/dashboard.html", {'user':user, 'appset': appset})

def edit_template(request):
    appset = AppSetting.objects.filter(user_id= request.user.id)
    return render(request, 'chat/pages/editpage/edittemplate.html' , {'appset':appset})



def profile(request):
    pro = AddUserProfile.objects.get(student_id=5)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=pro)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=pro)
    return render(request, 'chat/pages/profile.html', {'form':form})

def setting_view(request):
    appset = AppSetting.objects.filter(user_id= request.user.id)
    user = AddUser.objects.filter(user_id=request.user.id)
    integrate = FbIntegrate.objects.filter(user_id = request.user.id)
    company =AddCompany.objects.filter(user_id = request.user.id)
    return render(request, "chat/pages/setting_page.html" , {'user':user, 'integrate' :integrate ,'company':company , 'appset':appset})


def bot_view(request):
    appset = AppSetting.objects.filter(user_id= request.user.id)
    bot = BotSetting.objects.filter(user_id = request.user.id)
    return render(request, "chat/pages/bot.html", {'bot' :bot , 'appset' : appset})


def botset_view(request):
    appset = AppSetting.objects.filter(user_id= request.user.id)
    if request.method == "POST":
        form = BotSettingForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return redirect('chat:bot')
    else:
        form = BotSettingForm()
    return render(request, "chat/pages/bot_setting.html" , {'form': form ,'appset': appset } )


def lead_view(request):
    appset = AppSetting.objects.filter(user_id = request.user.id)
    company = AddCompany.objects.filter(user_id = request.user.id)
    return render(request, "chat/pages/lead.html" , {'company': company ,'appset': appset })






def add_company_view(request):
    appset = AppSetting.objects.filter(user_id = request.user.id)
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("chat:integrate")
    else:
        form = CompanyForm()
    return render(request, "chat/pages/add_company.html" , {'form' : form, 'appset': appset})

def delcompany(del_id):
    company = AddCompany.objects.get(pk=del_id)
    company.delete
    return redirect('chat:lead')

def editcompany(request, update_id):
    appset = AppSetting.objects.filter(user_id = request.user.id)
    company = AddCompany.objects.get(pk=update_id)
    if request.method == "POST":
        form = CompanyEditForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('chat:lead')
    else:
        form = CompanyEditForm(instance=company)
        return render(request,'chat/pages/editcompany.html', {'form': form ,  'appset': appset})

def integrate_view(request):
    appset = AppSetting.objects.filter(user_id = request.user.id)
    if request.method == "POST":
        form = IntegrateForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect("chat:setting")
    else:
        form = IntegrateForm()
    return render(request, "chat/pages/integrate.html" , {'form' : form ,'appset': appset })

def del_app(del_id):
    app = AppSetting.objects.get(pk= del_id)
    app.delete
    return redirect('chat:home')



def edit_appsetting(request, update_id):
    appset = AppSetting.objects.filter(user_id = request.user.id)
    appset1 = appset.get(pk=update_id)
    if request.method == "POST":
        form = AppSettingEditForm(request.POST, instance=appset1)
        if form.is_valid():
            form.save()
            return redirect('chat:home')
    else:
        form = AppSettingEditForm(instance=appset1)
        return render(request,'chat/pages/editpage/editappsetting.html', {'form': form ,  'appset': appset , 'appset1': appset1})






def app_setting_view(request):
    appset = AppSetting.objects.filter(user_id = request.user.id).first()
    # appset1 = AppSetting.objects.filter(user_id = request.user.id)

    if appset:
        form = AppSettingForm()
        error_message = "Cannot create another account. You already have one."
        render(request, 'chat/pages/app_setting.html', {'error_message': error_message , 'form': form })
        return redirect('chat:edit_template')
    if request.method == "POST": 
        form = AppSettingForm(request.POST , request.FILES)
        if form.is_valid():
           form.save()
           return redirect("chat:setting")   
    else:
        form = AppSettingForm()
        return render(request, "chat/pages/app_setting.html" , {'form' : form  })

def conversation(request):
    return render(request,'chat/pages/conversation.html')

def ask_openai( message , req):
    opena = BotSetting.objects.filter(user_id = req.user.id)[0]
    # openai_api_key = "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"
    openai.api_key =opena.api_key
    response = openai.ChatCompletion.create(
        model= opena.bot_model,
        messages=[
            {"role": "system", "content": opena.system_role},
            {"role": "user", "content": message},
        ],
    )
    answer = response.choices[0].message.content.strip()
    return answer


def chatboard_view(request):
    bot = BotSetting.objects.filter(user_id = request.user.id)[0]
    chats = Chat.objects.filter(user=request.user)
    appset = AppSetting.objects.filter(user_id = request.user.id)
    user = User.objects.filter(pk=request.user.id)
    # chats = Chat.objects.filter(user=request.user)

    if request.method == "POST":
        message = request.POST.get("message")
        response = ask_openai( message , request)
        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
         
        return JsonResponse({"message": message, "response": response})

    return render(request, "chat/pages/chatboard.html",  {'user':user , 'bot': bot , 'chats': chats, 'appset':appset})
