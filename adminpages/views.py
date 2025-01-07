from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,logout
from .forms import CustomteamMembersForm
from app.models import TeamMembers


# Create your views here.
@login_required(login_url='admin-login')
def admin_index(request):
    teams = TeamMembers.objects.all()
    return render(request, 'adminpages/admin_index.html',{'teams':teams})


@login_required(login_url='admin-login')
def create_team_member(request):
    form = CustomteamMembersForm()
    if request.method == 'POST':
        print('post request sending')
        print(request.POST)
        form = CustomteamMembersForm(request.POST, request.FILES)
        
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('admin-index')
    return render(request, 'adminpages/create_team.html', {'form': form})

def update_team_member(request, id):
    team = TeamMembers.objects.get(id=id)
    form = CustomteamMembersForm(instance=team)
    if request.method == 'POST':
        form = CustomteamMembersForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('admin-index')
    return render(request, 'adminpages/create_team.html', {'form': form})

def delete_team_member(request, id):
    team = TeamMembers.objects.get(id=id)
    team.delete()
    return redirect('admin-index')



def admin_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username,password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('admin-index')
    return render(request, 'adminpages/admin_login.html')

def admin_logout(request):
    logout(request)
    return redirect('admin-login')



