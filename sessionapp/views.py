from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class Input(View):
    def post(self,request):
        a=int(request.POST["t1"])
        b=int(request.POST["t2"])
        c=a+b
        request.session['res']=c
        request.session.set_expiry(60)
        s=HttpResponse("Data Submitted Successfully")
        return s
class Display(View):
    def get(self,request):
        if request.session.has_key('res'):
            z=request.session['res']
            return HttpResponse("The Sum Of Two Values Is::"+str(z))
        else:
            return render(request,'home.html')


