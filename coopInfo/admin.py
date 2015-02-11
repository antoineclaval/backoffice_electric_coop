from django.contrib import admin
from coopInfo.models import Cooperative , Person , State

class CooperativeAdmin(admin.ModelAdmin):
	list_display = ('name', 'stateId','website' )
	search_fields = ['name']
	list_filter = ['stateId']
	fieldsets = [
	    ('Basic info', {'fields': ['name', 'website', 'acronym']}),
	    ('Mail Info', {'fields': ['streetAddress', 'mailAddress']}),
	    ('Contact', {'fields': ['email', 'phone']}),
	    ('Administrative', {'fields':['bylaws','servingTime','nextElectionTerms','annualMeeting','montlyMeeting']}),
	    ('Misc', {'fields': ['consumers','numberOfEmployees','milesOfLines','countiesServed']})
	    ]

class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', 'ethnicity', 'coopId','title')
	search_fields = ['name']
	list_filter = ['ethnicity', 'title']

# Register your models here.
admin.site.register(Cooperative, CooperativeAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(State)