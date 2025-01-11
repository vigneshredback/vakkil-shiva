from django.shortcuts import render, HttpResponse
from app.models import TeamMembers

# Create your views here.
def index(request):
    team = TeamMembers.objects.filter(district='our attorneys')
    return render(request, 'app/index.html',{'teams':team})

def about(request):
    return render(request, 'app/about.html')

def attorney(request):
    team = TeamMembers.objects.filter(district='our attorneys')
    if request.method == 'POST':
        selected_district = request.POST.get('district')
        team = TeamMembers.objects.filter(district=selected_district)
        return render(request, 'app/attorney.html',{'teams':team,'selected_district':selected_district})
    print("get request")
    return render(request, 'app/attorney.html',{'teams':team,'selected_district':'chennai'})

def attorney_details(request,id):
    attorney = TeamMembers.objects.get(id=id)
    return render(request, 'app/attorney-details.html',{'attorney':attorney})

def contact(request):
    return render(request, 'app/contact.html')
def practice(request):
    return render(request, 'app/practice.html')

# below views are for practice

def practice_criminal_law(request):
    return render(request, 'app/practice/practice-criminal-law.html')
def practice_civil_law(request):
    return render(request, 'app/practice/practice-civil-law.html')
def practice_family_law(request):
    return render(request, 'app/practice/practice-family-law.html')

