import profile
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import ShortUrl, Profile
from .forms import CreateNewShortUrl, SignUpForm
from django.contrib.auth import login as dj_login , authenticate, logout as dj_logout
from datetime import datetime
import random, string


def home(request):
    if request.user.is_authenticated:
        user_urls = ShortUrl.objects.filter(profile__user__id = request.user.id)
        return render(request, 'home.html', {'msg':'Login successfuly!', 'user_urls':user_urls})
    return render(request, 'home.html')


def createshorturl(request):
    if request.method == 'POST':
        form = CreateNewShortUrl(request.POST)
        if form.is_valid():
            originalurl = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_digits_list = [str(i) for i in range(10)]
            random_chars = ''
            for i in range(3):
                random_chars += random.choice(random_chars_list)
                random_chars += random.choice(random_digits_list)
            while len(ShortUrl.objects.filter(short_url=random_chars)) != 0:
                for i in range(2):
                    random_chars += random.choice(random_chars_list)
                    random_chars += random.choice(random_digits_list)
            d = datetime.now()
            if request.user.is_authenticated:
                
                s = ShortUrl(original_url=originalurl, short_url=random_chars, time_date_created=d, profile= request.user.profile)
                s.save()
                return redirect(originalurl)
            return render(request, 'login.html')        

    else:
        form = CreateNewShortUrl()
        return render(request, 'create.html',{'form':form})



def redirect_url(request, url:str):
    try:
        current_obj = ShortUrl.objects.get(short_url=url)
        context = {'obj':current_obj}
        return render(request, 'redirect.html', context)
    except:
        return render(request, 'pagenotfound.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully!')

        return HttpResponse(f"{form.errors}") 

    form = SignUpForm()
    return render(request, 'signup.html', {'form':form})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            dj_login(request, user)
            user_urls = ShortUrl.objects.filter(profile__user__id = request.user.id)
            return render(request, 'home.html', {'msg':'Login successfuly!', 'user': user, 'user_urls':user_urls})
        return render(request, 'login.html', {'msg':'username or password is wrong!!!'})

    return render(request, 'login.html')



def logout(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return render(request, 'login.html')

        dj_logout(request)
        return render(request, 'home.html', {'msg':'See you later'})

    return render(request, 'home.html')



