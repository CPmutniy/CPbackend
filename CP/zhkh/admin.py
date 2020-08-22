from django.contrib import admin
from .models import *


admin.site.register(Company)
admin.site.register(Adress)
admin.site.register(Person)
admin.site.register(Voting)
admin.site.register(Question)
admin.site.register(Answer)