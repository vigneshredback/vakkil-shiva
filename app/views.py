from django.shortcuts import render, HttpResponse
from .models import TeamMenbers,Districts

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def attorney(request):
    teammembers = TeamMenbers.objects.filter(district_id=3)
    districts = Districts.objects.all()
    if request.method == 'POST':
        district = request.POST.get('district')
        selected_team = TeamMenbers.objects.filter(district_id=district)
        selected_district = Districts.objects.get(id=district)
        print("post request")
        return render(request, 'app/attorney.html',{'teammembers':teammembers,'districts':districts,'selected_team':selected_team,'selected_district':selected_district})
    print("get request")
    return render(request, 'app/attorney.html',{'teammembers':teammembers,'districts':districts})

def attorney_details(request,id):
    attorney = TeamMenbers.objects.get(id=id)
    return render(request, 'app/attorney-details.html',{'attorney':attorney})

