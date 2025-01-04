from django.contrib import admin
from . models import TeamMenbers,Consultants,Districts
# Register your models here.

admin.site.site_header = "VAKKIL SHIVA LAW ASSOCIATES"

admin.site.register(TeamMenbers)
admin.site.register(Consultants)
admin.site.register(Districts)
