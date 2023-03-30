from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def article(request):
    return HttpResponse("we are here to write article write anything ")


def about(request):
    return HttpResponse("This is About")

def Contact(request):
    return HttpResponse("contect us on anytime")