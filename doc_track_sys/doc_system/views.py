from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def my_doc(request):
    return render(request,"my_doc.html")

def document(request):
    return render(request,"document.html")

def profile(request):
    return render(request,"profile.html")

