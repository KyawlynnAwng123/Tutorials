from django.shortcuts import render,redirect
from django.http import JsonResponse
from Tutorials.models import Person,Town,Subject,User
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
# start homepage views
# @login_required(login_url='loginpage')
def homepageviews(request):
    new_search=request.GET.get('search') if request.GET.get('search') != None else ''

    towns=Town.objects.all()
    page=request.GET.get('p')
    
    persons=Person.persons.filter(
        Q(name__icontains=new_search)|
        Q(age__icontains=new_search)|
        Q(address__name__icontains=new_search)


        )

    


    paginator=Paginator(persons,3)
    # print(paginator.count)    
    # print(paginator.num_pages)    
    # # print(paginator.page_range)
    # for i in paginator.page_range:
    #     print(i)
    
  
    try:
        persons=paginator.page(page)
    
    except PageNotAnInteger:
        persons=paginator.page(1)
    
    except EmptyPage:
        persons=paginator.page(paginator.num_pages)   
    
    context={'persons':persons,
    'towns':towns,
    'paginator':paginator,
    'new_search':new_search
    
    }
    return render(request,'pages/home.html',context)
# end homepage views




# start createpage views

def createpageviews(request):
    towns=Town.objects.all()
    person=Person.persons.all()
    if request.method == 'POST':
        new_name=request.POST.get('name')
        # if new_name.is_num():
        #     return JsonResponse({'Username Error':'UserName must be a string'})
        new_age=request.POST.get('age')
        new_address=request.POST.get('address')
        
        new_image=request.FILES.get('image')
        # user=request.user

        Person.persons.create(
            name=new_name,
            age=new_age,
            address_id=new_address,
            image=new_image,
            # user=user,
            
        )
        messages.success(request, " မိတ်ဆွေ {} နာမေ နှင့် အသက် {} ကို အောင်မြင်စွာသိမ်းဆည်းပြီးပါဗျာလ်".format(new_name,new_age))
      
        return redirect('homepage')
    
        

    context={'towns':towns,'person':person}


    return render(request,'pages/create.html',context)
# end homepage views


# start editpage views
def editpageviews(request,pk):
    person=Person.persons.get(id=pk)
    towns=Town.objects.all()
    
    if request.method == 'POST':
        if request.FILES.get('image'):
            name=request.POST.get('name')
            address=request.POST.get('address')
            age=request.POST.get('age')
            image=request.FILES.get('image')

            person.name=name
            person.age=age
            person.address_id=address
            person.image=image  

            person.save()
            return redirect('homepage')
        name=request.POST.get('name')
        address=request.POST.get('address')
        age=request.POST.get('age')
        # image=request.FILES.get('image')

        person.name=name
        person.age=age
        person.address_id=address
        # person.image=image 

        person.save()
        return redirect('homepage')
    context={'person':person,'towns':towns}
    return render(request, 'pages/edit.html',context)
# end homepage views


# start deletepage views
def deletepageviews(request,pk):
    person=Person.persons.get(id=pk)
    person.delete()
    return redirect('homepage')
    context={'person':person}

    return render(request, 'pages/delete.html',context)
# end deletepage views

# start navbarpage views
def navbarpageviews(request):
    towns=Town.objects.all()
    context={'towns':towns}

    return render(request,'layout/navbar.html',context)
# end navbarpage views


# start eachtown pageviews
def eachtownpageviews(request,pk):
    new_search=request.GET.get('search') if request.GET.get('search') != None else ''

    

    
    persons=Person.persons.filter(
        Q(name__icontains=new_search)|
        Q(age__icontains=new_search)|
        Q(address__name__icontains=new_search)


        )
    address=Town.objects.get(id=pk)
    towns=Town.objects.all()
    person_in_eachtown=Person.persons.filter(address=address)

    context={'person_in_eachtown':person_in_eachtown,'towns':towns}
    return render(request,'pages/eachtown.html',context)
# end eachtown pageviews


# start detail pageviews
def detailpageviews(request,pk):
    towns=Town.objects.all()
    person=Person.persons.get(id=pk)
    context={'person':person,'towns':towns}
    return render(request, 'pages/detail.html',context)
# end detail pageviews


# start addtown pageviews
def addtownpageviews(request):
    towns=Town.objects.all()
    if request.method == 'POST':
        name=request.POST.get('town-name')
        Town.objects.create(
            name=name,
        )
        return redirect('homepage')
    context={'towns':towns}
    return render(request,'pages/add-town.html',context)
# end addtown pageviews



# start register pageviews
def register(request):
    register_form=UserForm()
    if request.method == 'POST':
        register_form=UserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('homepage')
    context={'register_form':register_form}
    return render(request,'accounts/register.html',context)
# end register pageviews


# start login pageviews
def loginpageviews(request):
    if request.method == 'POST':
        username=request.POST.get('name')
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username,password=password)
        except:
            messages.error(request, "User Does Not Exist")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, "User name or password incorrect")
            

    return render(request,'accounts/login.html')
# end login pageviews


# start logout pageviews
def logoutpageviews(request):
    logout(request)
    return redirect('loginpage')

    
    
# end logout pageviews








