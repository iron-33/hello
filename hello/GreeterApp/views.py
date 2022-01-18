from django.shortcuts import render
from django.http import HttpResponse
from .models import Name
from .forms import NameForm

def index(request):
    n=''
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            n=form.cleaned_data['name']
            for i in Name.objects.all():
                if i.name == n:
                    n="Вже бачилися, "+n
                    break
            else:
                n="Привіт, "+n
                form.save()

            print(n)
    users = Name.objects.all()
    form = NameForm()
    return render(request, 'GreeterApp/index.html',context= {'n':n, 'form' : form, 'users':users })
