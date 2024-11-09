from django.contrib import admin
from .models import Login, registration, Usm, assignment, lecture, Complaints, Feedbacks, Enquiry, noti,Adbranch,program

# Register your models here.
admin.site.register(Login)
admin.site.register(registration)
admin.site.register(Usm)
admin.site.register(assignment)
admin.site.register(lecture)
admin.site.register(Complaints)
admin.site.register(Feedbacks)
admin.site.register(Enquiry)
admin.site.register(noti)
admin.site.register(Adbranch)
admin.site.register(program)
