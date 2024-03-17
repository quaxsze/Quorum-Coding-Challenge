from django.contrib import admin

from .models import Bill, Legislator, Vote, VoteResult

admin.site.register(Bill)
admin.site.register(Legislator)
admin.site.register(Vote)
admin.site.register(VoteResult)
