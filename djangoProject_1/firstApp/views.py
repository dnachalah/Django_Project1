from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import FirstApp

# Create your views here.
#This code displays the login form.
def login(request):
    form = FirstApp.objects.all().values()
    template = loader.get_template('login.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

#This code ensures the email and password are valid.
def loginlog(request):
    email = request.POST.get('email')
    y = request.POST.get('pwd')
    error ="";
    

    try:
        match = FirstApp.objects.get(email=email,password=y)
        request.session['member_id'] = match.id
        request.session['username'] = match.firstname

        """
        if request.method == 'POST':
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
                return HttpResponse("You're logged in.")
            else:
                return HttpResponse("Please enable cookies and try again.")
        request.session.set_test_cookie()
        return render(request, 'foo/login.html')
        """

    except FirstApp.DoesNotExist:
        template = loader.get_template('login.html')
        context = {
            'error': "Invalid username or password.",
        }
        return HttpResponse(template.render(context, request))    
    return HttpResponseRedirect(reverse('index'))

def logout(request):
    try:
        del request.session['member_id']
        del request.session['username']
        template = loader.get_template('login.html')
        context = {
            'error': "You're logged out.",
        }
        return HttpResponse(template.render(context, request))
    except KeyError:
        pass
        
    #return HttpResponseRedirect(reverse('login'))

#This code displays the record of members in the database.
def index(request):
    mymembers = FirstApp.objects.all().values()
    reQ = request.session.get('username')      
    template = loader.get_template('indexx.html')
    context = {
        'mymembers': mymembers,
        'username': request.session.get('username')
    }
    if reQ == None:
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponse(template.render(context, request))

#This code displays the registration form page.
def add(request):
    template = loader.get_template('add.html')
    context = {
        'error': '',
    }
    return HttpResponse(template.render(context, request))

#This code ensures the password and confirm password are the same in the registration page, it also ensures the inputed email hasn't been used before.
def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    a = request.POST['email']
    b = request.POST['phone']
    c = request.POST['pwd']
    d = request.POST['pwdd']

#...ensures password and comfirm password match...
    if c != d:
        template = loader.get_template('add.html')
        context = {
            'error': 'Password does not match',
        }
        return HttpResponse(template.render(context, request))
    else:
        #...ensures inputed email hasn't been used before...
        try:
            match = FirstApp.objects.get(email=a)

            template = loader.get_template('add.html')
            context = {
                'error': "This email has been used. Try another one.",
            }
            return HttpResponse(template.render(context, request))

        except FirstApp.DoesNotExist:
            member = FirstApp(firstname=x, lastname=y, email=a, phone=b, password=c,)
            member.save()
        return HttpResponseRedirect(reverse('login'))

#This code displays the registration form page.
def edit(request, id):
    template = loader.get_template('edit.html')
    member = FirstApp.objects.get(id=id)
    
    context = {
        'error': '',
        "member": member
    }
    return HttpResponse(template.render(context, request))

#This code edits Username and Password
def editrecord(request,id):
    e = request.POST['nfirst']
    f = request.POST['nlast']
    g = request.POST['opwd']
    h = request.POST['npwd']
    i = request.POST['npwdd']
    j = request.POST['id']
    
    member = FirstApp.objects.get(id=j)
    if h != i:
        template = loader.get_template('edit.html')
        context = {
            'error': 'Passwords do not match',
            'member': member
        }
        #return HttpResponseRedirect(reverse('edit'))
        return HttpResponse(template.render(context, request))
    else:
        try:
            print(j)
            print(g)
            match = FirstApp.objects.get(id=j,password=g)

        except FirstApp.DoesNotExist:
            template = loader.get_template('edit.html')
            context = {
                'error': "Invalid password.",
                'member': member
            }
            return HttpResponse(template.render(context, request))
        member = FirstApp(firstname=e, lastname=f, email phone=member.phone, password=h, id=j,)
        member.save()
        return HttpResponseRedirect(reverse('index'))

#Ths code deletes members from the record.
def delete(request, id):
    member = FirstApp.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))
