from django.contrib import admin
from .models import Contact, Properties,Agents,Message
# Register your models here.
admin.site.register(Properties)
admin.site.register(Agents)
admin.site.register(Message)
admin.site.register(Contact)

# class MyModelAdmin(admin.ModelAdmin):

#     def get_readonly_fields(self, request, obj=None):
#         if obj: # editing an existing object
#             return self.readonly_fields + ('published')
#         return self.readonly_fields
