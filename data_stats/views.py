from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib  import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from data_stats.models import Category, Content, extendeduser,Political,Business,Technology
from .models import extendeduser
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.


def home(request):
    return HttpResponse("Hello")

def login(request):
    if request.method == "POST":
        uname = request.POST['uname']
        password = request.POST['password']
        user = auth.authenticate(username =uname,password =password)
        if user:
            auth.login(request,user)
            return redirect(check)
        else:
            print(request.POST['uname']+" ",request.POST['password'])
            return render(request,"login.html",{'error':'Wrong crendentials'})
    else:
        return render(request,"login.html",{'text': 'User'}) 
    

def admin_login_check(request):
     if request.method == "POST":
        uname = request.POST['uname']
        password = request.POST['password']
        get_user = User.objects.get(username=uname)
        if get_user.is_staff and get_user:
            user = auth.authenticate(username =uname,password =password)
            auth.login(request,user)
            return redirect(admin_dashboard)
        else:
            print(request.POST['uname']+" ",request.POST['password'])
            return render(request,"login.html",{'error':'You aren\'t admin'})
     else:
         return render(request,"login.html",{'text': 'Admin'}) 


@login_required(login_url='/login/admin/')
def admin_dashboard(request):
    return render(request,"admin/admin_dashboard.html")


def register(request):
    if request.method == "POST":
        try: 
            User.objects.get(username=request.POST['uname'])
            return render(request,"register.html",{'error':'User already registered'})
        except User.DoesNotExist:
            user = User.objects.create(username=request.POST['uname'])
            user.set_password(request.POST['password'])
            user.save()
            auth.login(request,user)
            return redirect(home)
    else:
        return render(request,'register.html')


def create_user(request):
    if request.method == "POST":
        try: 
            User.objects.get(username=request.POST['uname'])
            return render(request,"register.html",{'error':'User already registered'})
        except User.DoesNotExist:
            selected_category = request.POST['selected_category']
            user = User.objects.create_user(username=request.POST['uname'])
            user.set_password(request.POST['password'])
            user.save()
            newextendeduser = extendeduser(user_can_post=selected_category, user=user)
            newextendeduser.save()
            return redirect(create_user)
    all_users = User.objects.filter(is_staff = 0)
    categories = Category.objects.all()
    return render(request,'admin/create_user.html',context={'users':all_users,'categories':categories})


    

def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        summary = request.POST['summary']
        img_url = request.POST['img_url']
        content_url = request.POST['content_url']

        
        object_of_category = Category.objects.get(cat_id = (category))
        save_post = Content(category = object_of_category)
        save_post.save()
        return redirect(create_blog,{'message':'Post created Successfully!'})
    categories = Category.objects.all()
    return render(request ,'admin/create_blog.html', {'categories' : categories})

def delete_user(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect(create_user)    

def view_content(request,id,slug):
     if slug.lower() == 'technology':
        content = Technology.objects.get(id = id)
     elif slug.lower() == 'political':
         content = Political.objects.get(id = id)
     else:
        content = Business.objects.get(id = id)
     return render(request,"admin/view_content.html",{'content':content})


def show_news(request,slug,table_id):
    if int(table_id) is 1 :
        news = Technology.objects.all()
    elif int(table_id) is 2:
        news = Business.objects.all()
    else:
        news = Political.objects.all()
    
    return render(request,"admin/news_table.html",context={'news' : news,'slug':slug})
    
def delete_content(request,slug,id):
    if slug.lower() == 'technology':
        delete_it = Technology.objects.get(id = id)
    elif slug.lower() == 'political':
        delete_it = Political.objects.get(id = id)
    else:
        delete_it = Business.objects.get(id = id)
    
    delete_it.delete()
    return redirect(home)
    

def admin_logout(request):
    auth.logout(request)
    return redirect(admin_login_check)

''' ----------- ADMIN VIEW ENDED HERE -------------- '''






''' ALL USER VIEWS HERE '''

@login_required(login_url='/login/')
def create_user_blog(request):
    get_can_post = extendeduser.objects.get(user_id=request.user.id)    
    category = Category.objects.get(cat_id = get_can_post.user_can_post)        
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = int(request.POST['category'])
        summary = request.POST['summary']
        img_url = request.POST['img_url']
        content_url = request.POST['content_url']
        image = request.FILES['image']
        print(image)
        print('ghere')
        
        if category == 1:
            save_post = Technology(title=title, content=content,summary=summary,img_url=img_url,content_url=content_url,image=image,user_id = request.user.id,)
            save_post.save()
        elif category == 2:
            save_post = Business(title = title, content = content, user_id = request.user.id)
            save_post.save()
        else:
            save_post = Political(title = title, content = content, user_id = request.user.id)
            save_post.save()        
        return render(request,'users/user_create_blog.html',context={'message':'Post created Successfully!','categories' : category})
    
    return render(request ,'users/user_create_blog.html', {'categories' : category})


def update_content(request,id,slug):
    if slug.lower() == 'tech':
        content  = Technology.objects.get(id = id)
    elif slug.lower() == 'political':
        content = Political.objects.get(id = id)
    else:
        content = Business.objects.get(id = id)
        
    if request.method == 'POST':
        pass
    return render(request, 'users/update_content.html', {'content':content,})
    

@login_required(login_url='/login/')
def check(request):
    get_can_post = extendeduser.objects.get(user_id=request.user.id)    
    category = Category.objects.get(cat_id = get_can_post.user_can_post) 
    business_content = Business.objects.filter(user_id = request.user.id)
    political_content = Political.objects.filter(user_id = request.user.id)
    tech_content = Technology.objects.filter(user_id = request.user.id)
    context = {'business':business_content, 'political':political_content,
                'tech':tech_content,'category':category}
    return render(request,'users/users.html',context=context)


@login_required(login_url='/login/')
def user_logout(request):
    auth.logout(request)
    return redirect(login)


