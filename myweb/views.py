from django.shortcuts import render
from .models import register,blog
# Create your views here.

def index(request):
    return render(request,'index.html')
    

def regist(request):
   if(request.method=="POST"):
       if((request.POST.get('uname'))and(request.POST.get('name'))and(request.POST.get('pwd'))and(request.POST.get('mob'))and(request.POST.get('email'))):
        obj=register()
        obj.uname=request.POST.get('uname')
        obj.name=request.POST.get('name')
        obj.pwd=request.POST.get('pwd')
        obj.mobile=request.POST.get('mob')
        obj.email=request.POST.get('email')
        obj.question=request.POST.get('question')
        obj.answer=request.POST.get('answer')
        obj.save()
        return render(request,'login.html')
   else:
     return render(request,'register.html')


def login(request):
    if(request.method=="POST"):
       username=request.POST.get('uname')
       password=request.POST.get('pwd')
       try:
          if register.objects.get(uname=username,pwd=password):
            request.session['user']=username
            return render(request,'user.html')
          else:
            return render(request,'login.html')  
       except register.DoesNotExist:
          return render(request,'login.html')

    else:
       return render(request,'login.html')

def rstpwd(request):
    if(request.method=="POST"):
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        try:
            if register.objects.get(uname=username, pwd=password):

                npwd=request.POST.get('passn')
                register.objects.filter(uname=username).update(pwd=npwd)
                return render(request,'index.html')
        except register.DoesNotExist:
            return render(request,'rp.html')
    else:
        return render(request,'rp.html')
                 
def cblog(request):
    if (request.method == "POST"):
        if ((request.POST.get('bname')) and (request.POST.get('author')) and (request.POST.get('blog'))):
            obj =blog()
            obj.username=request.session['user']
            obj.bname = request.POST.get('bname')
            obj.author = request.POST.get('author')
            obj.blog = request.POST.get('blog')
            obj.save()
            return render(request, 'vblog.html')

    else:
        return render(request, 'blog.html')


def logout(request):
    try:
        del request.session["username"]
    except:
        pass
    return render(request,'login.html')