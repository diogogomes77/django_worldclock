from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from app.forms import UserForm, ChosenCountryForm, ChosenForm
from app.models import ChosenCountry, Chosen


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            if 'update' in request.POST:
                _mutable = data._mutable
                data._mutable = True
                data['profile_id'] = request.user.profile.id
                data._mutable = _mutable
                print('post= ' + str(data))
                chosen = Chosen.objects.get(pk=data['id'])
                chosen_form = ChosenForm(data=data, instance=chosen)
                if chosen_form.is_valid():
                    chosen_form.save()
                else:
                    print(chosen_form.errors)
            if 'delete' in request.POST:
                chosen = get_object_or_404(Chosen, pk=data['id'])
                chosen.delete()
            if 'create' in request.POST:
                _mutable = data._mutable
                data._mutable = True
                data['profile'] = request.user.profile.id
                data._mutable = _mutable
                print('create post= ' + str(data))
                new_chosen_form = ChosenForm(data=data)
                #chosen = new_chosen_form.save(commit=False)
                #chosen.profile = request.user.profile
                #chosen.save()
                if new_chosen_form.is_valid():
                    new_chosen_form.save()
                else:
                    print(new_chosen_form.errors)
        chosen_forms = []
        for chosen in request.user.profile.chosen.all():
            chosen_forms.append(ChosenForm(instance=chosen))

        form = ChosenForm(initial={'profile': request.user.profile})
        return render(request, 'app/index.html',
                      {'chosen_forms': chosen_forms,
                       'form': form
                       })
    return render(request,'app/index.html')

def index_(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            if 'update' in request.POST:
                _mutable = data._mutable
                data._mutable = True
                data['profile_id'] = request.user.profile.id
                data._mutable = _mutable
                print('post= ' + str(data))
                chosen = ChosenCountry.objects.get(pk=data['id'])
                chosen_form = ChosenCountryForm(data=data, instance=chosen)
                if chosen_form.is_valid():
                    chosen_form.save()
                else:
                    print(chosen_form.errors)
            if 'delete' in request.POST:
                chosen = get_object_or_404(ChosenCountry, pk=data['id'])
                chosen.delete()
            if 'create' in request.POST:
                _mutable = data._mutable
                data._mutable = True
                data['profile'] = request.user.profile.id
                data._mutable = _mutable
                print('create post= ' + str(data))
                new_chosen_form = ChosenCountryForm(data=data)
                #chosen = new_chosen_form.save(commit=False)
                #chosen.profile = request.user.profile
                #chosen.save()
                if new_chosen_form.is_valid():
                    new_chosen_form.save()
                else:
                    print(new_chosen_form.errors)
        chosen_forms = []
        for chosen in request.user.profile.chosencountry_set.all():
            chosen_forms.append(ChosenCountryForm(instance=chosen))

        form = ChosenCountryForm(initial={'profile': request.user.profile})
        return render(request, 'app/index.html',
                      {'chosen_forms': chosen_forms,
                       'form': form
                       })
    return render(request,'app/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        #profile_form = ProfileForm()
    return render(request, 'app/registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:

        return render(request, 'app/login.html', {})


def change_format(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            chosen_form = ChosenCountryForm(data=request.POST)
            if chosen_form.is_valid():
                chosen = chosen_form.save()
            else:
                print(chosen_form.errors)


