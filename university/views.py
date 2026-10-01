from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm
from service.models import Service

def homePage(request):
    ServicesData=Service.objects.all().order_by('service_title')[0:6]
    #before column name mean descending order without - mean ascending
    # for a in ServicesData:
    #     print(a.service_icon)
    # print(Service)
    data={
        'ServicesData':ServicesData

    }
    
    return render(request,'index.html',data)

def aboutUS(request):
    return HttpResponse("<b>Welcome to Wscubtech</b>")

def course(request):
    return HttpResponse("Django")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def about(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request, "about.html",{'output':output})


def courses(request):
    return render(request, "courses.html")


def facilities(request):
    return render(request, "facilities.html")


def contact(request):
    return render(request, "contact.html")

def saveevenodd(request):
    c=''
    
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request, "evenodd.html",{'error':True})
        
        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="Even Number"
        else:
            c="Odd Number"
    return render(request, "evenodd.html",{'c':c})

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
            elif opr=="%":
                c=n1%n2
        
    except:
        c="Invalid opr......"
    print(c)
    return render(request, "calculator.html",{'c':c})

def submitform(request):
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            n3=int(request.POST.get('num3'))
                
            finalans=n1+n2+n3
            # data={
            #     'n1':n1,
            #     'n2':n2,
            #     'output':finalans
            # }
            
            return HttpResponse(finalans)
    except:
        pass
    
def marksheet(request):
    if request.method=="POST":
        s1=eval(request.POST.get('subject1'))
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        s4=eval(request.POST.get('subject4'))
        s5=eval(request.POST.get('subject5'))
        
        t=s1+s2+s3+s4+s5
        
        p=t*100/500;
        if p>=60:
            d='First Div'
        elif p>=50:
            d='Second Div'
        elif p>=35:
            d='third Div'
        else:
            d='fail'
        data={
            'total':t,
            'per':p,
            'div':d,
        }
        print(t)
    return render(request, "marksheet.html",data)

def userForm(request):
    fn=usersForm()
    finalans = 0
    data={'form':fn}
    try:
        
        # For get method
        
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
        # n1=int(request.GET.get('num1'))
        # n2=int(request.GET.get('num2'))
        
        #for post method
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            n3=int(request.POST.get('num3'))
            
            finalans=n1+n2+n3
            data={
                'form':fn,
                'n1':n1,
                'n2':n2,
                'n3':n3,
                'output':finalans
            }
            
            url="/about/?output={}".format(finalans)
            # return HttpResponseRedirect(url)
            return redirect(url)
    except:
        pass 
    return render(request, "userForm.html",data)

# {'output':finalans}