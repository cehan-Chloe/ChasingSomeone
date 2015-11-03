__author__ = 'charleszhuochen'
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def user_login(request):

    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('ChasingSomeoneApp:user_home'))
            else:
                return HttpResponse('Your account does not active anymore.')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            errorMessage="Wrong user email or password."
            context_dict = {'error':True, 'errorMessage':errorMessage}
            return render(request, 'ChasingSomeoneApp/login.html', context_dict)

    else:
        return render(request, 'ChasingSomeoneApp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('ChasingSomeoneApp:user_login'))