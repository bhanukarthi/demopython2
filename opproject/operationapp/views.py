
from django.shortcuts import render


# Create your views here.
def demo(request):
    name="india"

    return render(request,"index.html",{'obj':name})
def result(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res=x+y
    res1=x-y
    res2=x*y
    res3=x/y

    return render(request,"result.html",{'addition':res,'substraction':res1,'multiplication':res2,'division':res3})

