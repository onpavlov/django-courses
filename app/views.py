from django.shortcuts import render, redirect
from django.views import View
from .models import Lot
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

class LotView(View):

    def list(request):
        # Render list of lots
        page = request.GET.get('page')
        lots = Lot().get_all(page=page)

        if (request.GET.get('logout') == 'true'):
            logout(request)

        return render(request, 'app/lot_list.html', {'lots': lots})

    def detail(request, id=id):
        lot = Lot().get_detail(pk=id)

        return render(request, 'app/lot_detail.html', {'lot': lot})

class UserView(View):

    def new(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            passwd = request.POST['password1']

            if form.is_valid() and passwd == request.POST['password2']:
                username = form.save()
                group = Group.objects.get(pk=2)
                user = User.objects.get(username=username)
                user.set_password(passwd) # setting password
                group.user_set.add(user.pk) # adding to group
                user.save()

                uauth = authenticate(username=username, password=passwd)

                if uauth != None:
                    login(request, uauth)
                    return redirect('/')
                else:
                    print('Error user login')
        else:
            form = UserRegisterForm()

        return render(request, 'app/user_register.html', {'form': form})

    def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            uauth = authenticate(username=username, password=password)

            if uauth != None:
                login(request, uauth)
                return redirect('/')
            else:
                print('Error user login')

        return render(request, 'app/user_login.html', {'form': UserLoginForm()})