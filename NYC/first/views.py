from django.shortcuts import render
from first.models import FeedbackForm, Cars, Music



def index(request):
    return render(request, 'main_page.html')

def about(request):
    return render(request, 'about.html')

def Wardrope(request):
    return render(request, 'Wardrope.html')

def music_base(request):
    data = Music.objects.all()
    return render(request, 'music_base.html', {"data":data})

#def music_bases(request,myid):
    data = Music.objects.filter(id = myid)
    return render(request, 'music_base.html', {"data": data})

def cars_base(request):
    data = Cars.objects.all()
    return render(request, 'cars_base.html', {"data": data})


#def cars_bases(request,myid):
    data = Cars.objects.filter(id = myid)
    return render(request, 'cars_base.html', {"data": data})




def contacts(request):
    if request.method == "POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        comment=request.POST["comment"]
        new = FeedbackForm(fname=request.POST["fname"],lname=request.POST["lname"],
                           email=request.POST["email"],comment=request.POST["comment"],)
        new.save()
        print(f"the name is {fname}, email : {email}")



    return render(request, 'contacts.html')