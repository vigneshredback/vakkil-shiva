from django.contrib import admin
from .models import TeamMembers,Districts,Consultants,Blog
# Register your models here.

admin.site.site_header = "VAKKIL SHIVA LAW ASSOCIATES"
admin.site.register(Consultants)
admin.site.register(Districts)
admin.site.register(TeamMembers)
admin.site.register(Blog)
