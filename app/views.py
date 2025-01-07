from django.shortcuts import render, HttpResponse
from app.models import TeamMembers

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def attorney(request):
    team = TeamMembers.objects.filter(district='chennai')
    if request.method == 'POST':
        selected_district = request.POST.get('district')
        team = TeamMembers.objects.filter(district=selected_district)
        return render(request, 'app/attorney.html',{'teams':team,'selected_district':selected_district})
    print("get request")
    return render(request, 'app/attorney.html',{'teams':team,'selected_district':'chennai'})

def attorney_details(request,id):
    attorney = TeamMembers.objects.get(id=id)
    return render(request, 'app/attorney-details.html',{'attorney':attorney})

