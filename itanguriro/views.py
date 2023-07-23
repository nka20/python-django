from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>home</h1>')

def guteranya(request,n1,n2):
    n1=int(n1)
    n2=int(n2)
    return HttpResponse(f'<h1> {n1} plus {n2} equal= {n1+n2}</h1>')


def igisoro(request,n1):
    response=""
    n1=int(n1) 
    for x in range(1,13):
     response += f"{x} * {n1}={n1*x} <br>"
    return HttpResponse(response)

def kugabura(request,n1,n2,n3):
    answer=""
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)
    for x in range(n1,int(n2),n3):
        #if(not(x % 2)==0):
            answer += f"{x} <br>"
    return HttpResponse(answer)


def premier(request,n1,n2):
    answer=""
    n1=int(n1)
    n2=int(n2)
    for x in range(n1,int(n2)):
        if is_prime(x):
            answer += f"{x} <br>"
    return HttpResponse(answer)