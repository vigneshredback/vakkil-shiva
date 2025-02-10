from django.shortcuts import render, HttpResponse
from app.models import TeamMembers,Districts,Consultants,Blog
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render


# Create your views here.
# def index(request):
#     team = TeamMembers.objects.filter(district_id=1)
#     return render(request, 'app/index.html',{'teams':team})


from django.shortcuts import render

def index(request):
    # Fetch team members
    team = TeamMembers.objects.filter(district_id=1)

    # Check if 'disclaimer_seen' exists in the session
    if not request.session.get('disclaimer_seen'):
        request.session['disclaimer_seen'] = True  # Set the session flag
        show_disclaimer = True  # Show the disclaimer
    else:
        show_disclaimer = False  # Hide the disclaimer
    
    # Pass the 'show_disclaimer' flag to the template
    return render(request, 'app/index.html', {'teams': team, 'show_disclaimer': show_disclaimer})



def about(request):
    return render(request, 'app/about.html')

def attorney(request):
    team = TeamMembers.objects.filter(district_id=1)
    district = Districts.objects.all()
    if request.method == 'POST':
        selected_district = request.POST.get('district')
        team = TeamMembers.objects.filter(district=Districts.objects.get(name=selected_district).id)
        return render(request, 'app/attorney.html',{'teams':team,'selected_district':selected_district,'districts':district})
    # print("get request")
    return render(request, 'app/attorney.html',{'teams':team,'selected_district':'chennai','districts':district})

def attorney_details(request,id):
    attorney = TeamMembers.objects.get(id=id)
    return render(request, 'app/attorney-details.html',{'attorney':attorney})

def contact(request):
    return render(request, 'app/contact.html')
# def practice(request):
#     return render(request, 'app/practice.html')

def blog(request):
    blogs_list = Blog.objects.all() 
    paginator = Paginator(blogs_list, 6) 

    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  

    return render(request, 'app/blog.html', {'page_obj': page_obj})

def blog_details(request, id):
    blog = get_object_or_404(Blog, id=id)
    recent_blogs = Blog.objects.order_by('-blog_date')[:5]
    return render(request, 'app/blog-details.html', {'blog': blog, 'recent_blogs': recent_blogs})


from django.core.paginator import Paginator
from django.shortcuts import render

def practice(request):
    # Define your static list of practices
    practices = [
        {"name": "Civil Law", "icon": "flaticon-law", "desc": "Our attorneys are highly trained and skilled in the Civil Law sector to provide the top service", "url": "practice-civil-law"},
        {"name": "Family Law", "icon": "flaticon-family", "desc": "Attorney of Our Squad is tremendously skillful to acquire a positive outcome and honest", "url": "practice-family-law"},
        {"name": "Business Law", "icon": "flaticon-inheritance", "desc": "You don’t need to worry about your business law till our Master’s Attorneys are here to help you", "url": "practice-business-law"},
        {"name": "Education Law", "icon": "flaticon-mortarboard", "desc": "Need Attorneys for Educational law? Then, here our Talented & Professionals Attorneys ready to serve you", "url": "practice-education-law"},
        {"name": "Criminal Law", "icon": "flaticon-auction", "desc": "We provide the Pre-Eminent Attorneys to solve the tough Criminal cases to help you", "url": "practice-criminal-law"},
        {"name": "Cyber Law", "icon": "flaticon-vulnerability", "desc": "We proffer cyber specialists attorneys who are brilliant in determining these types of cases", "url": "practice-cyber-law"},
        
        # Add more practices as needed

       {
            "name": "Admiralty and Maritime",
            "icon": "flaticon-auction",   # Icon mapped
            "desc": "Expert legal solutions for maritime disputes, shipping regulations, and international trade.",
            "url": "practice-admiralty-maritime",
        },
        {
            "name": "Antitrust & Competition",
            "icon": "flaticon-balance",
            "desc": "Comprehensive guidance on competition laws and antitrust issues to ensure fair practices.",
            "url": "practice-Antitrust-Competition",
        },
        {
            "name": "Compliance, Bribery & Anti-corruption",
            "icon": "flaticon-support", 
            "desc": "Safeguard your business with robust compliance strategies against bribery and corruption.",
            "url": "practice-compliance-bribery", 
        },
        {
            "name": "Corporate Insolvency & Restructuring",
            "icon": "flaticon-time",
            "desc": "Navigate insolvency and corporate restructuring with our expert legal team.",
            "url": "practice-corporate-insolvency",
        },
        {
            "name": "Employment & Industrial Relations",
            "icon": "flaticon-team",
            "desc": "Support for employment laws, workplace disputes, and industrial relations.",
            "url": "practice-employment-relations",
        },
        {
            "name": "Foreign Investment & Exchange Control",
            "icon": "flaticon-money-bag",
            "desc": "Legal advice on foreign investments and compliance with exchange control regulations.",
            "url": "practice-foreign-investment",
        },
        {
            "name": "Joint Ventures, Foreign & Technical Collaborations",
            "icon": "flaticon-conversation",
            "desc": "Structuring and negotiating successful joint ventures and collaborations.",
            "url": "practice-joint-ventures",
        },
        {
            "name": "Oil & Gas, Energy and Infrastructure",
            "icon": "flaticon-law",
            "desc": "Legal support for energy projects, oil and gas exploration, and infrastructure development.",
            "url": "practice-oil-gas",
        },
        {
            "name": "Project Finance",
            "icon": "flaticon-money-bag",
            "desc": "Comprehensive advice on financing large-scale infrastructure and industrial projects.",
            "url": "practice-project-finance",
        },
        {
            "name": "Regulatory Affairs",
            "icon": "flaticon-lawyer",
            "desc": "Navigate complex regulatory frameworks with our expert team.",
            "url": "practice-regulatory-affairs",
        },
        {
            "name": "Technology, Media & Telecommunication",
            "icon": "flaticon-email",
            "desc": "Specialized legal support for technology, media, and telecommunication sectors.",
            "url": "practice-tech-media",

        },
        {
            "name": "Aerospace and Defense",
            "icon": "flaticon-judge",
            "desc": "Expert guidance on aerospace contracts, defense procurements, and regulations.",
            "url": "practice-aerospace-defense",
        },
        {
            "name": "Banking & Finance",
            "icon": "flaticon-money-bag",
            "desc": "Comprehensive legal services for banking operations and financial transactions.",
            "url": "practice-banking-finance",

        },
        {
            "name": "Corporate Commercial Advisory",
            "icon": "flaticon-conversation",
            "desc": "End-to-end corporate advisory services for businesses of all scales.",
            "url": "practice-corporate-advisory",
        },
        {
            "name": "Dispute Resolution",
            "icon": "flaticon-auction",
            "desc": "Expert representation for arbitration, mediation, and litigation.",
            "url": "practice-dispute-resolution",
        },
        {
            "name": "Environment",
            "icon": "flaticon-law",
            "desc": "Guidance on environmental regulations and compliance.",
            "url": "practice-environment"
        },
        {
            "name": "Insurance & Reinsurance",
            "icon": "flaticon-checkmark",
            "desc": "Legal solutions for insurance claims, policies, and reinsurance matters.",
            "url": "practice-insurance"
        },
        {
            "name": "Intellectual Property",
            "icon": "flaticon-experience",
            "desc": "Protect your innovations with our expert intellectual property services.",
            "url": "practice-intellectual-property",
        },
        {
            "name": "Mergers & Acquisitions",
            "icon": "flaticon-law",
            "desc": "Expert assistance for mergers, acquisitions, and corporate restructuring.",
            "url": "practice-mergers-acquisitions"
        },
        {
            "name": "Mining & Resources",
            "icon": "flaticon-pin",
            "desc": "Legal solutions for mining projects, resource exploration, and environmental compliance.",
            "url": "practice-mining-resources"
        },
        {
            "name": "Private Equity, Venture Capital & Funds",
            "icon": "flaticon-money-bag",
            "desc": "Comprehensive services for private equity, venture capital, and fund management.",
            "url": "practice-private-equity",
        },
        {
            "name": "Real Estate",
            "icon": "flaticon-judge",
            "desc": "Expert guidance for real estate transactions, leasing, and development.",
            "url": "practice-real-estate",
        },
        {
            "name": "Taxation",
            "icon": "flaticon-auction",
            "desc": "Navigate tax complexities with our expert advisory and compliance services.",
            "url": "practice-taxation",
        },

    ]

    # Create Paginator object
    paginator = Paginator(practices, 6)  # Show 6 items per page

    # Get the current page number from the query string
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Get paginated items

    return render(request, 'app/practice.html', {'page_obj': page_obj})

# def practice_detail(request, practice_slug):
#     practices = [
#         {"name": "Civil Law", "icon": "flaticon-law", "desc": "Our attorneys are highly trained and skilled in the Civil Law sector to provide the top service", "url": "practice-civil-law"},
#         {"name": "Family Law", "icon": "flaticon-family", "desc": "Attorney of Our Squad is tremendously skillful to acquire a positive outcome and honest", "url": "practice-family-law"},
#         # Other practices...
#     ]

#     # Find the practice matching the slug
#     practice = next((item for item in practices if item["url"] == practice_slug), None)
    
#     # if not practice:
#     #     return HttpResponseNotFound("Practice not found")
    
#     return render(request, 'app/practice_detail.html', {'practice': practice})



# below views are for practice

def practice_criminal_law(request):
    return render(request, 'app/practice/practice-criminal-law.html')
def practice_civil_law(request):
    return render(request, 'app/practice/practice-civil-law.html')
def practice_family_law(request):
    return render(request, 'app/practice/practice-family-law.html')
def practice_business_law(request):
    return render(request, 'app/practice/practice-business-law.html')
def practice_education_law(request):
    return render(request, 'app/practice/practice-education-law.html')
def practice_cyber_law(request):
    return render(request, 'app/practice/practice-cyber-law.html')
def practice_admiralty_maritime_law(request):
    return render(request, 'app/practice/practice-admiralty-maritime.html')
def practice_Antitrust_Competition_law(request):
    return render(request, 'app/practice/practice-Antitrust-Competition.html')
def practice_compliance_bribery_law(request):
    return render(request, 'app/practice/practice-compliance-bribery.html')
def practice_corporate_insolvency_law(request):
    return render(request, 'app/practice/practice-corporate-insolvency.html')
def practice_employment_relations_law(request):
    return render(request, 'app/practice/practice-employment-relations.html')
def practice_foreign_investment_law(request):
    return render(request, 'app/practice/practice-foreign-investment.html')
def practice_joint_ventures_law(request):
    return render(request, 'app/practice/practice-joint-ventures.html')
def practice_oil_gas_law(request):
    return render(request, 'app/practice/practice-oil-gas.html')
def practice_project_finance_law(request):
    return render(request, 'app/practice/practice-project-finance.html')
def practice_regulatory_affairs_law(request):
    return render(request, 'app/practice/practice-regulatory-affairs.html')
def practice_tech_media_law(request):
    return render(request, 'app/practice/practice-tech-media.html')
def practice_aerospace_defense_law(request):
    return render(request, 'app/practice/practice-aerospace-defense.html')
def practice_banking_finance_law(request):
    return render(request, 'app/practice/practice-banking-finance.html')
def practice_corporate_advisory_law(request):
    return render(request, 'app/practice/practice-corporate-advisory.html')
def practice_dispute_resolution_law(request):
    return render(request, 'app/practice/practice-dispute-resolution.html')
def practice_environment_law(request):
    return render(request, 'app/practice/practice-environment.html')
def practice_insurance_law(request):
    return render(request, 'app/practice/practice-insurance.html')
def practice_intellectual_property_law(request):
    return render(request, 'app/practice/practice-intellectual-property.html')
def practice_mergers_acquisitions_law(request):
    return render(request, 'app/practice/practice-mergers-acquisitions.html')
def practice_mining_resources_law(request):
    return render(request, 'app/practice/practice-mining-resources.html')
def practice_private_equity_law(request):
    return render(request, 'app/practice/practice-private-equity.html')
# def practice_real_estate_law(request):
#     return render(request, 'app/practice/practice-admiralty-maritime.html')
def practice_real_estate_law(request):
    return render(request, 'app/practice/practice-real-estate.html')
def practice_taxation_law(request):
    return render(request, 'app/practice/practice-taxation.html')



# views.py

# from django.core.mail import send_mail
# from django.shortcuts import render, redirect
# from django.contrib import messages

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phone_number')
#         msg_subject = request.POST.get('msg_subject')
#         message = request.POST.get('message')

#         # Construct the email content
#         email_subject = f"New Contact Form Submission: {name}"
#         email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone_number}\nSubject: {msg_subject}\nMessage:\n{message}"

#         try:
#             send_mail(email_subject, email_message, email, ['giridharanredbackit@gmail.com'])
#             messages.success(request, 'Your message has been sent successfully!')
#         except Exception as e:
#             messages.error(request, f'An error occurred: {e}')

#         return redirect('contact')

#     return render(request, 'app/contact.html')



# views.py

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        msg_subject = request.POST.get('msg_subject')
        message = request.POST.get('message')

        # Construct the email content
        email_subject = f"New Contact Form Submission: {name}"
        email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone_number}\nSubject: {msg_subject}\nMessage:\n{message}"

        try:
            send_mail(email_subject, email_message, email, ['giridharanredbackit@gmail.com'])
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')

        return redirect('contact')

    return render(request, 'app/contact.html')

def index_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        msg_subject = request.POST.get('msg_subject')
        message = request.POST.get('message')

        # Construct the email content
        email_subject = f"New Contact Form Submission: {name}"
        email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone_number}\nSubject: {msg_subject}\nMessage:\n{message}"

        try:
            send_mail(email_subject, email_message, 'giridharanredbackit@gmail.com', ['giridharanredbackit@gmail.com'])
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')

        return redirect('index')

    return render(request, 'app/index.html')


